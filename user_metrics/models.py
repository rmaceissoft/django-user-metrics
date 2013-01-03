from datetime import date
from django.db import models
from django.contrib.auth.models import User

from user_metrics.utils import get_quarter_number


class Metric(models.Model):
    """ holds the types of metrics
    """
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    name = models.CharField(max_length=90)

    def __unicode__(self): return self.name


class MetricItem(models.Model):
    """ more atomic representation of a metric by each user
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=1)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric,
            count = self.count,
            date_up = self.date_up.strftime("%b. %d %Y")
        )
        if self.user:
            string = u"%(count)s '%(name)s' by %(user)s for %(date_up)s"
            values["user"] = self.user
        else:
            string = u"%(count)s '%(name)s' for %(date_up)s"
        return string % values


class MetricDay(models.Model):
    """ represent aggregation of metrics daily
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric.name,
            date_up = self.date_up.strftime("%b. %d %Y")
        )
        if self.user:
            string =  "'%(name)s' by %(user)s for %(date_up)s"
            values['user'] = self.user
        else:
            string = "'%(name)s' for '%(date_up)s'"
        return string % values


class MetricWeek(models.Model):
    """ represent aggregation of metric weekly
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric.name,
            week = self.date_up.strftime("%U"),
            year = self.date_up.strftime("%Y")
        )
        if self.user:
            string =  "'%(name)s' by %(user)s for week %(week)s of year %(year)s"
            values['user'] = self.user
        else:
            string = "'%(name)s' for week %(week)s of year %(year)s"
        return string % values


class MetricMonth(models.Model):
    """ represent aggregation of metrics monthly
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric.name,
            month = self.date_up.strftime("%B"),
            year = self.date_up.strftime("%Y")
        )
        if self.user:
            string =  "'%(name)s' by %(user)s for %(month)s %(year)s"
            values['user'] = self.user
        else:
            string = "'%(name)s' for %(month)s %(year)s"
        return string % values


class MetricQuarter(models.Model):
    """ represent aggregation of metrics by quarter
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric.name,
            quarter = get_quarter_number(self.date_up, True),
            year = self.date_up.strftime("%Y")
        )
        if self.user:
            string =  "'%(name)s' by %(user)s for quarter %(quarter)s of year %(year)s"
            values['user'] = self.user
        else:
            string = "'%(name)s' for %(year)s"
        return string % values


class MetricYear(models.Model):
    """ represent aggregation of metrics by year
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        values = dict(
            name = self.metric.name,
            year = self.date_up.strftime("%Y")
        )
        if self.user:
            string =  "'%(name)s' by %(user)s for %(year)s"
            values['user'] = self.user
        else:
            string = "'%(name)s' for %(year)s"
        return string % values

