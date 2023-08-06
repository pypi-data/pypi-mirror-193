import datetime as dt
from datetime import datetime
from collections import defaultdict
import calendar
from typing import Dict, List, Union

from babel import UnknownLocaleError
from babel.dates import format_datetime
from dateutil import relativedelta
from dateutil.rrule import rrule, WEEKLY, SU as SUNDAY
import pytz


__all__ = (
    'MONTHS',
    'HOURS',
    'SWITCH_HOURS',
    'HOUR_CHOICES',
    'SWITCH_HOUR_CHOICES',
    'get_current_month',
    'get_current_day',
    'today',
    'get_now',
    'get_now_repr',
    'get_month_name',
    'get_months_name',
    'get_month_days_quantity',
    'get_month_days',
    'get_dates_amount_in_period',
    'get_dates_in_period',
    'get_years_in_period',
    'get_split_dates_in_period',
    'get_periods_for_each_month',
    'get_readable_date',
    'get_date_obj_from_str',
    'get_time_obj_from_int',
    'get_date_delta_months',
    'get_date_delta_days',
    'convert_date_to_datetime',
    'convert_datetime_to_date',
    'is_today',
    'is_future',
    'is_past',
    'is_tomorrow',
    'is_after_tomorrow',
    'is_all_dates_in_period',
    'is_all_dates_in_available_years',
    'is_all_dates_in_month',
    'is_leap_year',
    'get_last_sunday',
    'get_switch_dates',
    'is_switch_date',
    'get_serialized_switch_dates',
)

# CONSTANTS
LAST = -1
FIRST = 0
SECOND = 1

DATE_FORMAT = '%d.%m.%Y'
DATETIME_FORMAT = '%d-%m-%Y_%H:%M'

MONTHS = {
    'JANUARY': 1,
    'FEBRUARY': 2,
    'MARCH': 3,
    'APRIL': 4,
    'MAY': 5,
    'JUNE': 6,
    'JULY': 7,
    'AUGUST': 8,
    'SEPTEMBER': 9,
    'OCTOBER': 10,
    'NOVEMBER': 11,
    'DECEMBER': 12
}

today = datetime.now().date()

HOURS = [i for i in range(1, 25)]
SWITCH_HOURS = [i for i in range(1, 26)]

HOUR_CHOICES = [(x, '{}'.format(x + 1)) for x in range(0, 24)]
SWITCH_HOUR_CHOICES = [(x, '{}'.format(x + 1)) for x in range(0, 25)]


def get_current_day() -> dt.date:
    return datetime.now().date()


def get_current_month() -> int:
    return datetime.now().month


def get_now(tz: str = None) -> datetime:
    """
    tz:
        default: 'EET' (Eastern Europe)

    Return:
        now or None if timezone unavailable
    """
    tz = tz or 'EET'

    try:
        tz = pytz.timezone(tz)
        return datetime.now(tz=tz)
    except Exception as e:
        pass


def get_now_repr(format_: str = DATETIME_FORMAT) -> str:
    """ Default date format is "%d-%m-%Y_%H-%M" """
    try:
        return datetime.now().strftime(format_)
    except Exception as e:
        pass


def get_month_name(month: int, locale: str = 'en') -> str:
    """
    Return month name by specific locale (English by default)

    Examples
        get_month_name(7) -> 'July'
        get_month_name(7, 'uk') -> 'Липень'
    """
    try:
        date = datetime.strptime(str(month), '%m')
        month_name = (
            format_datetime(
                date,
                format='LLLL',
                locale=locale
            ).capitalize()
        )
        return month_name
    except (UnknownLocaleError, ValueError):
        pass


def get_months_name(locale: str = 'en') -> List[str]:
    """ Return months name by specific locale (English by default) """
    try:
        return [get_month_name(i, locale) for i in range(1, 13)]
    except Exception as e:
        pass


def get_month_days_quantity(year: int, month: int) -> int:
    """ Return days quantity in a specific month """
    try:
        return calendar.monthrange(year, month)[SECOND]
    except (TypeError, calendar.IllegalMonthError):
        pass


def get_month_days(year: int, month: int) -> List[dt.date]:
    num_days = get_month_days_quantity(year, month)
    if num_days:
        days = [dt.date(year, month, day) for day in range(1, num_days + 1)]
        return days


def get_readable_date(date: dt.date, format_: str = DATE_FORMAT) -> str:
    """ Default date format is "%d.%m.%Y" """
    try:
        date = date.strftime(format_)
        return date
    except AttributeError:
        pass


def get_date_obj_from_str(string_: str, format_: str = DATE_FORMAT) -> dt.date:
    """ Default date format is "%d.%m.%Y" """
    try:
        return datetime.strptime(string_, format_).date()
    except (ValueError, TypeError):
        pass


def get_dates_amount_in_period(
    period_from: dt.date,
    period_to: dt.date
) -> int:
    try:
        return (period_to - period_from).days
    except Exception:
        pass


def get_dates_in_period(
    period_from: dt.date,
    period_to: dt.date
) -> List[dt.date]:
    try:
        dates = [
            period_from + dt.timedelta(days=x)
            for x in range((period_to - period_from).days + 1)
        ]
        return dates
    except (TypeError, AttributeError):
        pass


def get_years_in_period(
    period_from: dt.date,
    period_to: dt.date
) -> List[int]:
    try:
        years = [i for i in range(period_from.year, period_to.year + 1)]
        return years
    except AttributeError:
        pass


def get_split_dates_in_period(
    period_from: dt.date,
    period_to: dt.date
) -> Dict[int, Dict[int, List[dt.date]]]:
    period_dates = get_dates_in_period(period_from, period_to)
    if period_dates:
        dates = defaultdict(lambda: defaultdict(list))
        [dates[date.year][date.month].append(date) for date in period_dates]
        return dates


def get_periods_for_each_month(
    period_from: dt.date,
    period_to: dt.date
) -> Dict[int, Dict[int, Dict[str, Union[dt.date, List[dt.date]]]]]:
    """
    Return years -> months -> days

    Example output
    {
        2022: {
            1: {
                'from': 01.01.2022,
                'to': 31.01.2022,
                'days': [01.01.2022, 02.02.2022, ..., 31.01.2022]
            },
            2: {
                'from': 03.02.2022,
                'to': 28.02.2022,
                'days': [03.02.2022, ..., 28.02.2022]
        },
        2023: {
            1: {
                'from': 01.01.2023,
                'to': 01.01.2023,
                'days': [01.01.2023]
            }
        }
    }
    """
    dates_in_period = get_split_dates_in_period(period_from, period_to)

    if dates_in_period:
        periods = defaultdict(lambda: defaultdict(dict))
        for year, months in dates_in_period.items():
            for m, days in months.items():
                periods[year][m] = {
                    'from': days[FIRST],
                    'to': days[LAST],
                    'days': days
                }
        return periods


def get_time_obj_from_int(time: int) -> dt.time:
    """
    Accept digits from 0 to 23

    Examples
        get_time_obj_from_int(0) -> 'datetime.time(0, 0)'
    """
    try:
        time = dt.time(time)
        return time
    except (TypeError, ValueError):
        pass


def get_date_delta_days(
    date: dt.date,
    days: int,
    vector: str = 'next'
) -> dt.date:
    """
    Vector choices: 'next' or 'previous'
    Default: 'next'
    """
    if vector in ('next', 'previous'):
        try:
            delta = relativedelta.relativedelta(days=days)
            if vector == 'next':
                date += delta
            else:
                date -= delta
            return date
        except TypeError:
            pass


def get_date_delta_months(
    date: datetime,
    months: int,
    vector: str
) -> dt.date:
    """ Vector choices: 'next' or 'previous'"""
    if vector in ('next', 'previous'):
        try:
            delta = relativedelta.relativedelta(months=months)
            if vector == 'next':
                date += delta
            else:
                date -= delta
            return date
        except TypeError:
            pass


def convert_date_to_datetime(date: dt.date) -> datetime:
    try:
        return datetime.combine(date, datetime.min.time())
    except TypeError:
        pass


def convert_datetime_to_date(date_time: datetime) -> dt.date:
    try:
        return date_time.date()
    except AttributeError:
        pass


def is_leap_year(year: int) -> bool:
    try:
        return calendar.isleap(year)
    except TypeError:
        pass


def is_today(date: dt.date) -> bool:
    return date == today


def is_future(date: dt.date) -> bool:
    return date > today


def is_past(date: dt.date) -> bool:
    return date < today


def is_tomorrow(date: dt.date) -> bool:
    current_day = get_current_day()
    tomorrow = get_date_delta_days(current_day, days=1)

    return date == tomorrow


def is_after_tomorrow(date: dt.date) -> bool:
    current_day = get_current_day()
    after_tomorrow = get_date_delta_days(current_day, days=2)

    return date == after_tomorrow


def is_all_dates_in_period(
    dates: List[dt.date],
    period_from: dt.date,
    period_to: dt.date
) -> bool:
    period_dates = get_dates_in_period(period_from, period_to)
    if period_dates:
        for i in dates:
            if i not in period_dates:
                return False
        return True


def is_all_dates_in_available_years(
    dates: List[dt.date],
    years: List[int]
) -> bool:
    try:
        return all([i.year in years for i in dates])
    except AttributeError:
        pass


def is_all_dates_in_month(dates: List[dt.date], month: int) -> bool:
    return all([i.month == month for i in dates])


def get_last_sunday(year: int, month: int) -> dt.date:
    try:
        date = dt.date(year=year, month=month, day=1)
    except TypeError:
        return None  # noqa

    # can't be more then 5 sundays in month
    days = rrule(freq=WEEKLY, dtstart=date, byweekday=SUNDAY, count=5)

    last_sunday = days[LAST]

    if last_sunday.month != month:
        last_sunday = days[LAST - 1]

    return last_sunday.date()


def get_switch_dates(year: int) -> Dict[int, dt.date]:
    """Return dict of march and october last sunday dates"""
    march = get_last_sunday(year, 3)
    october = get_last_sunday(year, 10)
    return {3: march, 10: october}


def is_switch_date(d: dt.date) -> bool:
    """ Return true if date is last Sunday of March or October """
    return d in get_switch_dates(d.year).values()


def get_serialized_switch_dates(year: int) -> Dict[int, str]:
    """
    Output example: {3: '25.03.2022', 10: '28.10.2022'}
    """
    dates = get_switch_dates(year=year)
    dates = {k: get_readable_date(v) for k, v in dates.items()}
    return dates
