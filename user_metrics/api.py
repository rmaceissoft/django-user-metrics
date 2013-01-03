from user_metrics.models import Metric, MetricItem
from user_metrics.utils import get_backend


def put_metric(slug, user=None, count=1, **kwargs):
    """ Increment a metric by a given user """
    backend = get_backend()
    backend.put_metric(slug, user=user, count=count, **kwargs)