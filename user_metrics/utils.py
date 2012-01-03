import datetime

def week_for_date(date):
    return date - datetime.timedelta(days=date.weekday())
