from django.conf import settings


USER_METRICS_BACKEND = getattr(settings, 'USER_METRICS_BACKEND', 'user_metrics.backends.db')

# mixpanel backend
USER_METRICS_MIXPANEL_API_URL = getattr(settings, 'USER_METRICS_MIXPANEL_API_URL', 'http://api.mixpanel.com/track/')
USER_METRICS_MIXPANEL_TOKEN = getattr(settings, 'USER_METRICS_MIXPANEL_TOKEN', None)
USER_METRICS_MIXPANEL_API_KEY = getattr(settings, 'USER_METRICS_MIXPANEL_API_KEY', None)
USER_METRICS_MIXPANEL_API_SECRET = getattr(settings, 'USER_METRICS_MIXPANEL_API_SECRET', None)