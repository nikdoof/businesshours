from datetime import datetime, timedelta, time


def calc_business_hours(start, end, weekdays=(1, 2, 3, 4, 5), hours=range(8, 18)):
    """Calculates the number of seconds hours between two dates"""

    def date_range(start_date, end_date):
        """Converts two datetimes into a list of dates between them"""
        if isinstance(start_date, datetime):
            start_date = start_date.date()
        if isinstance(end_date, datetime):
            end_date = end_date.date()
        if start_date > end_date:
            raise ValueError('You provided a start_date that comes after the end_date.')
        while True:
            yield start_date
            start_date = start_date + timedelta(days=1)
            if start_date > end_date:
                break

    if start.date() == end.date():
        if not start.date().isoweekday() in weekdays:
            return 0
        if start.time().hour in hours:
            actual_start = start
        else:
            if start.time().hour >= hours[-1] + 1:
                return 0
            actual_start = datetime.combine(start.date(), time(hours[0], 0, 0))
        if end.time().hour in hours:
            actual_end = end
        else:
            if end.time().hour <= hours[0]:
                return 0
            actual_end = datetime.combine(end.date(), time(hours[-1] + 1, 0, 0))
        secs = (actual_end - actual_start).total_seconds()
        return secs
    else:
        total_seconds = 0
        dates = [dt for dt in date_range(start, end)]

        for idx, dt in enumerate(dates):
            day_start = datetime.combine(dt, time(0, 0, 0))
            day_end = datetime.combine(dt, time(23, 59, 59))
            if idx == 0:
                day_start = start
            if idx == len(dates) - 1:
                day_end = end
            total_seconds += calc_business_hours(day_start, day_end, weekdays, hours)
        return total_seconds
