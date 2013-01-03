from django.contrib import admin

from user_metrics.models import Metric, MetricItem, MetricDay, MetricWeek, MetricMonth, MetricQuarter, MetricYear
from user_metrics.utils import get_quarter_number


class MetricItemAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'date_up')
    list_filter = ('metric', 'user')


class MetricDayAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'when', )
    list_filter = ('metric', 'user', )

    def when(self, obj):
        return obj.date_up
    when.short_description = u'When'
    when.admin_order_field = 'date_up'


class MetricWeekAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'when', )
    list_filter = ('metric', 'user', )

    def when(self, obj):
        return u"Week %(week)s of year %(year)s" % {
            'week': obj.date_up.strftime("%U"),
            'year': obj.date_up.strftime("%Y")
        }
    when.short_description = u'When'
    when.admin_order_field = 'date_up'


class MetricMonthAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'when', )
    list_filter = ('metric', 'user', )

    def when(self, obj):
        return obj.date_up.strftime("%B %Y"),
    when.short_description = u'When'
    when.admin_order_field = 'date_up'


class MetricQuarterAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'when', )
    list_filter = ('metric', 'user', )

    def when(self, obj):
        return u"Quarter %(quarter)s of %(year)s" % {
            'quarter': get_quarter_number(obj.date_up, True),
            'year': obj.date_up.year
        }
    when.short_description = u'When'
    when.admin_order_field = 'date_up'


class MetricYearAdmin(admin.ModelAdmin):
    list_display = ('metric', 'user', 'count', 'when', )
    list_filter = ('metric', 'user', )

    def when(self, obj):
        return obj.date_up.strftime('%Y')
    when.short_description = u'When'
    when.admin_order_field = 'date_up'


admin.site.register(Metric)
admin.site.register(MetricItem, MetricItemAdmin)
admin.site.register(MetricDay, MetricDayAdmin)
admin.site.register(MetricWeek, MetricWeekAdmin)
admin.site.register(MetricMonth, MetricMonthAdmin)
admin.site.register(MetricQuarter, MetricQuarterAdmin)
admin.site.register(MetricYear, MetricYearAdmin)