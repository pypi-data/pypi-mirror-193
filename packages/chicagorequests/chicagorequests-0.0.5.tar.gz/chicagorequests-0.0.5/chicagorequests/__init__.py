import datetime
import json
import logging
import multiprocessing.dummy
import sys
import warnings
import zoneinfo
from typing import Any, Generator, Iterable

import click
import requests.adapters
import scrapelib
import tabulate
import tqdm

from .request_types import request_types

Interval = Iterable[tuple[datetime.datetime, datetime.datetime]]


class APIScraper(scrapelib.Scraper):
    def request(self, method, url, **kwargs):
        response = super().request(method, url, **kwargs)

        self._check_errors(response)

        return response

    def _check_errors(self, response):

        try:
            response.json()
        except json.decoder.JSONDecodeError:
            response.status_code = 500
            raise scrapelib.HTTPError(response)


class Downloader:
    BASE_URL = "http://311api.cityofchicago.org/open311/v2/requests.json"

    def __init__(
        self, request_type=None, updated_start_date=None, updated_end_date=None
    ):

        self._session = None

        if request_type:
            self.args = {
                "extensions": "true",
                "service_code": ",".join(request_type),
            }
        else:
            self.args = {
                "extensions": "true",
            }

        if updated_start_date:
            self.args.update(
                {
                    "updated_after": updated_start_date,
                    "updated_before": updated_end_date,
                }
            )

    @property
    def session(self):
        if not self._session:
            self._session = APIScraper(
                requests_per_minute=0, retry_attempts=5, retry_wait_seconds=10
            )
            self._session.timeout = 30

        return self._session

    def prepare_args(
        self, start: datetime.datetime, end: datetime.datetime, page_size: int
    ) -> dict[str, Any]:
        args = self.args.copy()
        args.update(
            {
                "start_date": start.isoformat(),
                "end_date": end.isoformat(),
                "page": 1,
                "page_size": page_size,
            }
        )
        return args

    def __call__(
        self, interval: tuple[datetime.datetime, datetime.datetime]
    ) -> list[dict[str, Any]]:
        start, end = interval
        results = []
        page_size = 200
        args = self.prepare_args(start, end, page_size)
        try:
            page = self.session.get(self.BASE_URL, params=args).json()
        except scrapelib.HTTPError as e:
            warnings.warn(
                "Could not load {url}. We will miss some requests from {date}".format(
                    url=e.response.request.url, date=start.date()
                )
            )
            page = []
        results.extend(page)

        while len(page) == page_size:
            args["page"] += 1
            try:
                page = self.session.get(self.BASE_URL, params=args).json()
            except scrapelib.HTTPError as e:
                warnings.warn(
                    "Could not load {url}. We will miss some requests from {date}".format(
                        url=e.response.request.url, date=start.date()
                    )
                )
                page = []
            results.extend(page)

        return results


def day_intervals(
    start_datetime: datetime.datetime, end_datetime: datetime.datetime
) -> Generator[tuple[datetime.datetime, datetime.datetime], None, None]:

    start = start_datetime
    while start < end_datetime:
        yield start, datetime.datetime.combine(start, datetime.time.max).replace(
            tzinfo=start.tzinfo
        )
        start += datetime.timedelta(days=1)


def validate_request_type(ctx, _, types):
    for r_type in request_types:
        if r_type not in request_types:
            raise click.BadParameter(
                f"{r_type} is not a valid request type. To see valid types run 'chicagorequests --list-request-types'"
            )
    return [request_types[r_type]["service_code"] for r_type in types]


def list_request_types(ctx, _, show_list):
    if show_list:
        table = tabulate.tabulate(
            [(k, v["service_name"]) for k, v in request_types.items()],
            headers=["type", "definition"],
            maxcolwidths=40,
        )
        click.echo(table)
        sys.exit()


def set_logging_level(ctx, _, verbose):
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)


def prepare_early_time(ctx, _, early_time):
    if early_time:
        early_time = datetime.datetime.combine(early_time, datetime.time.min).replace(
            tzinfo=zoneinfo.ZoneInfo("America/Chicago")
        )
    return early_time


def prepare_late_time(ctx, _, late_time):
    if late_time:
        late_time = datetime.datetime.combine(late_time, datetime.time.max).replace(
            tzinfo=zoneinfo.ZoneInfo("America/Chicago")
        )
    return late_time


def default_intervals(
    start_date,
    end_date,
    updated_start_date,
    updated_end_date,
):

    EARLIEST_DATE = datetime.datetime(2018, 7, 18).replace(
        tzinfo=zoneinfo.ZoneInfo("America/Chicago")
    )
    TODAY = prepare_late_time(None, None, datetime.datetime.today())

    if end_date:
        if start_date and start_date >= end_date:
            raise click.UsageError("--end-date must be after --start-date")
        elif end_date < EARLIEST_DATE:
            sys.exit()
        elif end_date > TODAY:
            end_date = TODAY
        elif not start_date:
            start_date = EARLIEST_DATE

    if start_date and not end_date:
        end_date = TODAY

    if updated_end_date:
        if updated_start_date and updated_start_date >= updated_end_date:
            raise click.UsageError(
                "--updated-end-date must be after --updated-start-date"
            )
        elif updated_end_date < EARLIEST_DATE:
            sys.exit()
        elif updated_end_date > TODAY:
            updated_end_date = TODAY
        elif not updated_start_date:
            updated_start_date = EARLIEST_DATE

    if updated_start_date and not updated_end_date:
        updated_end_date = TODAY

    if not start_date and not updated_start_date:
        start_date = prepare_early_time(None, None, datetime.datetime.today())
        end_date = TODAY
    elif updated_start_date and not start_date:
        start_date = EARLIEST_DATE
        if updated_end_date:
            end_date = updated_end_date
        else:
            end_date = TODAY

    return start_date, end_date, updated_start_date, updated_end_date


@click.command()
@click.option(
    "-s",
    "--start-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="the first day of the time range to check for created service requests",
    callback=prepare_early_time,
)
@click.option(
    "-e",
    "--end-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="the last day of the time range to check for created service requests",
    callback=prepare_late_time,
)
@click.option(
    "--updated-start-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="the first day of the time to check for updated service requests",
    callback=prepare_early_time,
)
@click.option(
    "--updated-end-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="the last day of the time to check for updated service requests",
    callback=prepare_late_time,
)
@click.option(
    "-t",
    "--request-type",
    multiple=True,
    help="service types to fetch",
    callback=validate_request_type,
)
@click.option(
    "-v", "--verbose", count=True, help="verbosity level", callback=set_logging_level
)
@click.option(
    "--list-request-types",
    is_flag=True,
    default=False,
    help="list valid request types",
    callback=list_request_types,
)
def main(
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    updated_start_date: datetime.datetime,
    updated_end_date: datetime.datetime,
    verbose: int,
    request_type,
    list_request_types,
) -> None:
    """Download service requests from the Chicago Open311 API. By
    default, today's requests of all types. Will write service
    requests as line-delimited JSON to stdout."""

    start_date, end_date, updated_start_date, updated_end_date = default_intervals(
        start_date, end_date, updated_start_date, updated_end_date
    )

    intervals = day_intervals(start_date, end_date)

    downloader = Downloader(
        request_type=request_type,
        updated_start_date=updated_start_date,
        updated_end_date=updated_end_date,
    )

    with multiprocessing.dummy.Pool(15) as pool:
        for day in tqdm.tqdm(
            pool.imap_unordered(downloader, intervals),
            total=(end_date - start_date).days + 1,
            colour="#228b22",
            unit="day",
        ):
            for result in day:
                click.echo(json.dumps(result))
