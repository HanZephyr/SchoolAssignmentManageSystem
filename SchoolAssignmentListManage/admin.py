# -*- coding: UTF-8 -*-
from django.contrib import admin
from datetime import datetime, timedelta

# Register your models here.

from SchoolAssignmentListManage.models import *

from import_export import resources

#
# @admin.register(ScheduleName)
# class ScheduleNameAdmin(admin.ModelAdmin):
#     # pk：索引
#     # 属性 list_display 表示要显示哪些属性
#     list_display = ['pk', 'course_name']
#     list_display_links = ('pk', 'course_name')
#
#     ordering = ('pk',)


class EndTimeListFilter(admin.SimpleListFilter):
    title = u'最近截止'
    parameter_name = 'EndTime'

    def lookups(self, request, model_admin):
        return (
            ('0', u'最近7天'),
            ('1', u'最近10天'),
            ('2', u'最近15天'),
            ('3', u'最近30天'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.now().date()

        if self.value() == '0':
            # 前一天日期
            day = cur_date + timedelta(days=7)
            return queryset.filter(end_time__lte=day)
        elif self.value() == '1':
            day = cur_date + timedelta(days=10)
            return queryset.filter(end_time__lte=day)
        elif self.value() == '2':
            day = cur_date + timedelta(days=15)
            return queryset.filter(end_time__lte=day)
        elif self.value() == '3':
            day = cur_date + timedelta(days=30)
            return queryset.filter(end_time__lte=day)


class TimeOutListFilter(admin.SimpleListFilter):
    title = u'是否超时（默认 未截止）'
    parameter_name = 'TimeOut'

    def lookups(self, request, model_admin):
        return (
            ('0', u'未截止'),
            ('1', u'已截止'),
            ('2', u'所有'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.now()
        seven_days_ago = cur_date - timedelta(days=7)

        print('self.value()：', self.value())

        if self.value() == '0' or not self.value():
            # 前一天日期
            return queryset.exclude(end_time__isnull=False,
                                    end_time__lt=cur_date).exclude(end_time__isnull=True, start_time__lte=seven_days_ago)
        elif self.value() == '1':
            return queryset.exclude(end_time__isnull=False,
                                    end_time__gte=cur_date).exclude(end_time__isnull=True, start_time__gt=seven_days_ago)
        elif self.value() == '2':
            day = cur_date + timedelta(days=15)
            return queryset


class AssignmentInfoResource(resources.ModelResource):
    class Meta:
        model = AssignmentInfo


@admin.register(AssignmentInfo)
class AssignmentInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'course_name',
                    'assignmentInfo', 'start_time', 'end_time']

    search_fields = ('assignmentInfo',)

    list_filter = ('course_name', EndTimeListFilter,
                   TimeOutListFilter, 'end_time')

    list_display_links = ('pk', 'course_name')

    list_editable = ('assignmentInfo', 'start_time', 'end_time')

    fieldsets = [(None, {'fields': ['course_name', 'assignmentInfo', 'start_time', 'end_time']}),
                 (u'其他信息', {
                     'fields': ['additionalInfo', 'file', 'image']})]

    ordering = ('end_time', '-start_time')


admin.site.site_title = '教学管理后台'
admin.site.site_header = '教学管理后台'
