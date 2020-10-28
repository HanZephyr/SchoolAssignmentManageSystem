# -*- coding: UTF-8 -*-


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from django.db.models.query import QuerySet
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
from json import dumps
from .models import *
from Course.models import Course


# def get_assignment(request, assignment_type, days=None):

@api_view(('GET',))
def get_assignments(request):
    """获取每周作业
    :param request: 请求
    # :param assignment_type: 获取作业类型（info：使用说明，week：本周未超时作业，all_effective：所有未超时，today：当天发布的作业）
    # :param days: 最近几天的作业（当 assignment_type 为 days 时，必须输入 days）
    """

    global resQueryset, res_end_time_Queryset, res_end_time_null_Queryset
    assignment_type = request.GET.get(
        'assignment_type', default='all_effective')

    # 获取数据库信息
    this_week_start = datetime.now() - timedelta(days=datetime.now().weekday())  # 星期一日期
    if assignment_type == 'info':
        info = [
            '<h1>使用说明</h1>',
            '<p><b>assignment_type:</b> 获取作业类型（<b>info：</b>使用说明，<b>week：</b>本周未超时作业，<b>all_effective：</b>所有未超时），<b>today：</b>当天发布的作业）</p>',
            '<p><b>days:</b> 最近几天的作业（当 assignment_type 为 days 时，必须输入 days 参数，表示最近几天）</p>'
        ]
        response = '\n'.join(info)
        return HttpResponse(response)
    elif assignment_type == 'all_effective':
        cur_date = datetime.now().date()

        res_end_time_Queryset = AssignmentInfo.objects.filter(
            end_time__isnull=False, end_time__gte=cur_date)
        res_end_time_null_Queryset = AssignmentInfo.objects.filter(
            end_time__isnull=True, start_time__gte=this_week_start)

    elif assignment_type == 'week':
        cur_date = datetime.now()
        this_week_end = datetime.now() - timedelta(days=datetime.now().weekday() - 6)
        print(this_week_end)
        res_end_time_Queryset = AssignmentInfo.objects.filter(
            Q(end_time__isnull=False, start_time__gte=this_week_start, end_time__gte=cur_date) |
            Q(end_time__isnull=False, end_time__gte=cur_date,
              end_time__lte=this_week_end)
        )

        res_end_time_null_Queryset = AssignmentInfo.objects.filter(end_time__isnull=True,
                                                                   start_time__gte=this_week_start)
    elif assignment_type == 'days':
        cur_date = datetime.now()
        days = request.GET.get('days', default=None)
        if days:
            day = cur_date + timedelta(days=int(days))
            print(day)
            res_end_time_Queryset = AssignmentInfo.objects.filter(
                end_time__isnull=False, end_time__lte=day, end_time__gte=cur_date)
            res_end_time_null_Queryset = AssignmentInfo.objects.none()

        else:
            return HttpResponseNotFound(content='<h1>请正确传入参数：days（天数）！</ph1')
    elif assignment_type == 'today':
        cur_date = datetime.now()
        year = cur_date.year
        month = cur_date.month
        day = cur_date.day
        cur_date_start = datetime(year, month, day)
        cur_date_end = datetime(year, month, day + 1)
        res_end_time_Queryset = AssignmentInfo.objects.filter(
            start_time__gte=cur_date_start,
            start_time__lt=cur_date_end
        )
        res_end_time_null_Queryset = AssignmentInfo.objects.none()

    course_name_queryset = Course.objects.all().values_list()
    print(course_name_queryset)
    if not course_name_queryset.values_list().count():
        return HttpResponseNotFound(content='<h1>课程名称列表 为空！</h1>')

    course_name_dict = dict(tuple((item[0], item[1]) for item in course_name_queryset))

    print('course_name_dict：', course_name_dict)
    assignment_dict = dict()

    if not (res_end_time_Queryset.values_list().count() or res_end_time_null_Queryset.values_list().count()):
        return HttpResponseNotFound(content='<h1>有效作业列表 为空！</h1>')

    if res_end_time_Queryset and res_end_time_Queryset.values_list().count():
        for assignment in res_end_time_Queryset.values_list():
            course_name = course_name_dict[assignment[1]]
            # print('!!!')
            # print(f"（截止时间：{assignment[4].strftime(' ')}）" if assignment[4] else '')
            # print('!!!')
            if course_name not in assignment_dict:
                assignment_dict[course_name] = [assignment[2] +
                                                (f"（截止时间：{assignment[4].strftime('%m{M}%d{D} %H:%M').format(M='月', D='日')}）" if assignment[4] else '')
                                                ]
            else:
                assignment_dict[course_name].append(
                    assignment[2] +
                    (f"（截止时间：{assignment[4].strftime('%m{M}%d{D} %H:%M').format(M='月', D='日')}）" if assignment[4] else '')
                )

    if res_end_time_null_Queryset and res_end_time_null_Queryset.values_list().count():
        for assignment in res_end_time_null_Queryset.values_list():
            course_name = course_name_dict[assignment[1]]

            if course_name not in assignment_dict:
                assignment_dict[course_name] = [assignment[2]]
            else:
                assignment_dict[course_name].append(assignment[2])

    print('assignment_dict', assignment_dict)

    return HttpResponse(dumps(assignment_dict))
