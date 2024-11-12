"""library/datetime

Why datetime module?
    - Some years don't have the same number of days: leap year
    - Months don't have the same number of days
    - Each day does not have the same number of hours (daylight time saving)
        - Not all countries have daylight time saving
        - And those that do, may apply it at a different moemnt in time
    - Time zones
    - in short, it's a big mess

Most computer systems start counting time from an arbitrary point in time called
the UNIX epoch (January 1st 1970 at 00:00:00 hours UTC)

Documentations:
    - https://docs.python.org/3/library/datetime.html
    - https://docs.python.org/3/library/zoneinfo.html
    - https://github.com/stub42/pytz.git
    - https://pendulum.eustace.io/docs
        - https://github.com/sdispater/pendulum
YouTube Videos:
    - https://www.youtube.com/watch?v=TFa38ONq5PY

Some Interesting Links about Time and Timezones:
    - The Largely Untold Story Of How One Guy In California Keeps The World’s Computers
      Running On The Right Time Zone. (Well, Sort Of)
      https://onezero.medium.com/the-largely-untold-story-of-how-one-guy-in-california-keeps-the-worlds-computers-on-the-right-time-a97a5493bf73
    - The Problem with Time & Timezones - Computerphile
      https://www.youtube.com/watch?v=-5wpm-gesOY
"""

import time
from datetime import datetime
from builtins import print as p


def main() -> int:

    # --------------------------------------------------------------------------
    # Get UNIX timestamp
    # - time module

    now = time.time()  # Returns floating point number

    # 1731368823.173461
    # ^<second> .^<fraction of second>

    now_ns = time.time_ns()  # More preice in nano seconds (returns integer)

    # -------------------------------------------------------------------------
    # FACT: Older 32-bit computers store UNIX time as an integer of size 32
    # bits. As a result, at specifically 3:14:7 AM on January 19th 2038, the
    # 32-bit integer is going to overflow!
    #
    # Although Python uses dynamically size integer, it under the hood uses OS
    # function (syscalls) to get the current time; There still going to be a
    # problem due to that.
    #
    # To avoid problem: Make sure to use a 64-bit computer by then.

    # ------------------------------------------------------------------------------
    # UTC:
    #
    # - UNIX time is expressed in UTC time zone:
    # - UTC stands for (Universal Time Coordinated or coordinated universal
    #   time)
    # - Before 1972 it was called Greenwich Mean Time (GMT)
    # - It's not adjusted for the daylight saving time; There's always 24 hours
    #   in a day.
    # - It's also called "z-time" or "Zulu time"
    # - Python: 'datetime' module

    from datetime import datetime  # NOTE: datetime is a class

    some_date = datetime(2024, 11, 12, 10, 0, 0)  # 2024-11-12 10:00:00

    # -------------------------------------------------------------------------
    # Since python 3.6 datetime supports ISO 8601 parsing.
    #

    some_date = datetime.fromisoformat("2024-11-12T10:00:00")  # 2024-11-12 10:00:00

    # -------------------------------------------------------------------------
    # Comparing dates
    #

    before_or_after = some_date < datetime.now()  # True

    # -------------------------------------------------------------------------
    # Date and time objects can be broadly divided into categories:
    # 1. aware (contains timezone information -> timezone-aware)
    # 2. naive (does not contain timezone information -> timezone-naive)
    # By default datetime objects are timezone-naive. It can be timezone-aware by passing timezone
    # information object to 'tzinfo' parameter of datetime constructor.
    #
    # - Prior to Python3.9 there was no builtin package for timezones -> pip install pytz
    # - Python3.9 added a builtin zoneinfo module since then pytz is deprecated!

    import pytz

    utc = pytz.timezone("UTC")  # Create a UTC timezone info object
    loc = utc.localize(dt=some_date)  # get a datetime localized to a specific timezone

    # or

    from zoneinfo import ZoneInfo

    loc = datetime(2024, 11, 12, 10, 0, 0, tzinfo=ZoneInfo("UTC"))

    # timezone-naive: # 2024-11-12 10:00:00
    # timezone-aware: # 2024-11-12 10:00:00+00:00

    # -------------------------------------------------------------------------
    # List of all timezones

    from pytz import country_names, country_timezones

    all_timezones = [country_timezones.get(country) for country in country_names]

    # or

    from zoneinfo import available_timezones

    all_timezones = available_timezones()

    # -------------------------------------------------------------------------
    # Convert between timezones
    #

    tehran_tz = pytz.timezone("Asia/Tehran")

    # or

    tehran_tz = ZoneInfo("Asia/Tehran")

    # UTC time -> local time
    tehran_time = datetime.now().astimezone(tehran_tz)  # 2024-11-12 13:30:00+03:30
    # 2024-11-12 04:16:13.062482+03:30

    amsterdam_tz = ZoneInfo("Europe/Amsterdam")
    amsterdam_time = tehran_time.astimezone(amsterdam_tz)
    # 2024-11-12 01:46:13.062482+01:00

    # -------------------------------------------------------------------------
    # Limitations of datetime package
    #
    # 1. There are lots of different modules and types: datetime, calendar,
    #    dateutil, timedelta, ... -> it gets confusing quickly for advanced
    #    programs.
    # 2. Timezone objects need to be created for timezone conversions
    # 3. No humanizing dates and no durations
    #
    # 3rd party packges created to deal with some of these limitations:
    # - arrow
    # - delorean
    # - pendulum: drop-in replacement for datetime class
    # These packages offer a nicer interface than the datetime package

    # -------------------------------------------------------------------------
    # Pendulum
    #
    # 1. adds simpler timezone handling
    # 2. datetime objects are timezone aware by default
    # 3. has features like localization, human-readable version of timezones
    #
    # pip install pendulum

    ...

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
