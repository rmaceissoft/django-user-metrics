from django.conf import settings


USER_METRICS_BACKEND = getattr(settings, 'USER_METRICS_BACKEND', 'user_metrics.backends.db')
