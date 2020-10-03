from django.contrib import admin

# Register your models here.

from datetime import datetime, timedelta

from .models import *

from import_export import resources


@admin.register(TermInfo)
class TermInfoAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'term_name',
        'start_date', 'end_date',
        'week_counts'
    ]

    search_fields = ('term_name', 'start_date', 'end_date')

    # list_filter = ('course_name', EndTimeListFilter,
    #                TimeOutListFilter, 'end_time')
    list_filter = ('term_name', )

    list_display_links = ('pk', 'term_name')

    list_editable = ('start_date', 'end_date', 'week_counts')

    # fieldsets = [(None, {'fields': ['term_name', 'start_time', 'end_time', 'week_counts', 'current_week']}),
    #              (u'其他信息', {
    #                  'fields': ['additionalInfo', 'upload_file']})]

    ordering = ('-start_date', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'name',
        'gender'
    ]

    search_fields = ('name',)

    list_filter = ('gender',)

    list_display_links = ('pk', 'name')

    list_editable = ('gender',)

    ordering = ('pk',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'course_name',
        'teacher', 'assessment_method'
    ]

    search_fields = ('course_name', 'teacher__name')

    list_filter = ('teacher', 'assessment_method')

    list_display_links = ('pk', 'course_name')

    list_editable = ('teacher', 'assessment_method')

    ordering = ('pk',)


@admin.register(LessonSchedule)
class LessonScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'title',
        'start_time', 'end_time'
    ]

    search_fields = ('title',)

    list_display_links = ('pk', 'title')

    list_editable = ('start_time', 'end_time')

    ordering = ('pk', )


@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'course',
        'week_day', 'classroom',
        'weeks', 'lesson',
        'is_suspend'
    ]

    search_fields = ('course__course_name', 'classroom')

    list_filter = ('course', 'week_day', 'classroom', 'lesson', 'is_suspend')

    list_display_links = ('pk', 'course')

    list_editable = ('is_suspend',)

    # ordering = ('-start_date', )
    ordering = ('pk',)


admin.site.site_title = '教学管理后台'
admin.site.site_header = '教学管理后台'

