# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/13 11:57
# @Author: 韩家旭
# @File  : urls.py

from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = '[Course]'

urlpatterns = [
    # path('get_assignments/', views.get_assignments)
    url(r'^course/$',
        views.CourseSchedule.as_view({
            'get': 'get_day_course',
        }), name='get_day_course'),
]
