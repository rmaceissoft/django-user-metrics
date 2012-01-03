import datetime

from user_metrics.models import MetricWeek

def week_for_date(date):
    return date - datetime.timedelta(days=date.weekday())


def total_weeks_aggregated():
    """
    return total of weeks aggregates to MetricWeek model
    """
    try:
        first_week = MetricWeek.objects.all().order_by('-date_up')[0].date_up
    except IndexError:
        first_week = week_for_date(datetime.date.today())
    return (datetime.date.today() - first_week).days / 7

