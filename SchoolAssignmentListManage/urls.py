# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/13 11:57
# @Author: 韩家旭
# @File  : urls.py

from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = '[SchoolAssignmentListManage]'

urlpatterns = [
    path('get_assignments/', views.get_assignments)
]
