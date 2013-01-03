import base64
import urllib
import urllib2
import json

from user_metrics import settings


def put_metric(slug, user=None, count=1, **kwargs):
    """ Increment a metric by a given user """
    if "token" not in kwargs:
        kwargs["token"] = settings.USER_METRICS_MIXPANEL_TOKEN
    if user:
        kwargs['$bucket'] = user.id

    params = {"event": slug, "properties": kwargs}
    b64_data = base64.b64encode(json.dumps(params))

    data = urllib.urlencode({"data": b64_data})
    req = urllib2.Request(settings.USER_METRICS_MIXPANEL_API_URLurl, data)
    for i in xrange(count):
        response = urllib2.urlopen(req)
        if response.read() == '0':
            raise Exception(u'MixPanel returned 0')
