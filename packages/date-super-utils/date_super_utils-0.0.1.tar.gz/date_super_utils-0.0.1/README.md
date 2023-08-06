# Date utils


Constants:
```
- MONTHS: {'JANUARY': 1, ..., 'DECEMBER': 12}

- HOURS: [1, 2, ..., 24]

- SWITCH_HOURS: [1, 2, ..., 25]

- HOUR_CHOICES: [(0, 1), (1, 2), ..., (23, 24)]

- SWITCH_HOUR_CHOICES: [(0, 1), (1, 2), ..., (24, 25)]

- DATE_FORMAT = '%d.%m.%Y'

- DATETIME_FORMAT = '%d-%m-%Y_%H:%M'

- today: datetime.datetime.date obj
```

Methods:
```
- get_current_month
- get_current_day
- get_now
- get_now_repr
- get_month_name
- get_months_name
- get_month_days_quantity
- get_month_days
- get_dates_amount_in_period
- get_dates_in_period
- get_years_in_period
- get_split_dates_in_period
- get_periods_for_each_month
- get_readable_date
- get_date_obj_from_str
- get_time_obj_from_int
- get_date_delta_months
- get_date_delta_days
- convert_date_to_datetime
- convert_datetime_to_date
- is_today
- is_future
- is_past
- is_tomorrow
- is_after_tomorrow
- is_all_dates_in_period
- is_all_dates_in_available_years
- is_all_dates_in_month
- is_leap_year
- get_last_sunday
- get_switch_dates
- is_switch_date
- get_serialized_switch_dates
```