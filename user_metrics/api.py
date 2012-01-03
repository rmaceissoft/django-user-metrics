from user_metrics.models import Metric, MetricItem

def put_metric(slug, user, count=1, **kwargs):
    """ Increment a metric by a given user """

    try:
        metric = Metric.objects.get(slug=slug)
    except Metric.DoesNotExist:
        metric = Metric.objects.create(slug=slug, name=slug)

    MetricItem.objects.create(
        metric = metric,
        user = user,
        count = count
    )