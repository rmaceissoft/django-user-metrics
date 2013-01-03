import datetime
from django.core.management.base import NoArgsCommand

from user_metrics.models import Metric, MetricItem, MetricDay, MetricWeek, MetricMonth, MetricQuarter, MetricYear
from user_metrics.utils import week_for_date, month_for_date, quarter_for_date, year_for_date

class Command(NoArgsCommand):
    help = "Aggregate Application Metrics"

    def handle_noargs(self, **options):
        """ Aggregate Metrics by User """

        # Aggregate Items
        items = MetricItem.objects.all()

        for item in items:
            # Daily Aggregation
            metric_day, create = MetricDay.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = item.date_up
            )
            metric_day.count = metric_day.count + item.count
            metric_day.save()

            # Weekly Aggregation
            week_date = week_for_date(item.date_up)
            metric_week, create = MetricWeek.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = week_date
            )
            metric_week.count = metric_week.count + item.count
            metric_week.save()

            # Monthly aggregation
            month_date = month_for_date(item.date_up)
            metric_month, create = MetricMonth.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = month_date
            )
            metric_month.count = metric_month.count + item.count
            metric_month.save()

            # Quarter aggregation
            quarter_date = quarter_for_date(item.date_up)
            metric_quarter, create = MetricQuarter.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = quarter_date
            )
            metric_quarter.count = metric_quarter.count + item.count
            metric_quarter.save()

            # Yearly aggregation
            year_date = year_for_date(item.date_up)
            metric_year, create = MetricYear.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = year_date
            )
            metric_year.count = metric_year.count + item.count
            metric_year.save()

        # remove all metric items
        items.delete()
