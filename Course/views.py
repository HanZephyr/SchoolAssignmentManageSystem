from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from .models import *
from .CourseSerializer import CourseSerializer


class CourseSchedule(ModelViewSet):
    def get_day_course(self, request, *args, **kwargs):
        params = request.query_params
        if 'weekday' not in params:
            res_json = {
                'code': 412,
                'msg': '失败，缺少 weekday 参数'
            }
            return JsonResponse(res_json, json_dumps_params={'ensure_ascii': False})
        else:
            weekday = params['weekday']
        if 'week_count' not in params:
            this_week_start = datetime.now() - timedelta(days=datetime.now().weekday())
            start_study_day = datetime.strptime(
                str(TermInfo.objects.all().order_by('-start_date').first().start_date),
                '%Y-%m-%d'
            )
            week_count = int((this_week_start - start_study_day).days / 7 + 1)
        else:
            week_count = params['week_count']

        ClassSchedule_QuerySet = ClassSchedule.objects.filter(
            Q(week_day=weekday) &
            Q(is_suspend=False)
        )
        ClassSchedule_QuerySet_Serializer = CourseSerializer(instance=ClassSchedule_QuerySet,
                                                             many=True,
                                                             context={'request': request})

        ClassSchedule_data = ClassSchedule_QuerySet_Serializer.data
        class_schedule_list = list(filter(lambda x: str(week_count) in x['weeks'].split(','), ClassSchedule_data))

        res_json = {
            'code': 0,
            'msg': '成功',
            'data': class_schedule_list
        }
        return JsonResponse(res_json, json_dumps_params={'ensure_ascii': False})
