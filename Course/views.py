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
        if 'week_day' in params:
            week_day = params['week_day']
        else:
            week_day = datetime.now().weekday() + 1
        if 'week_count' in params:
            week_count = params['week_count']
        else:
            this_week_start = datetime.now() - timedelta(days=datetime.now().weekday())
            start_study_day = datetime.strptime(
                str(TermInfo.objects.all().order_by('-start_date').first().start_date),
                '%Y-%m-%d'
            )
            week_count = int((this_week_start - start_study_day).days / 7 + 1)
        ClassSchedule_QuerySet = ClassSchedule.objects.filter(
            Q(week_day=week_day) &
            Q(is_suspend=False)
        ).order_by('lesson__start_time')
        ClassSchedule_QuerySet_Serializer = CourseSerializer(instance=ClassSchedule_QuerySet,
                                                             many=True,
                                                             context={'request': request})

        ClassSchedule_data = ClassSchedule_QuerySet_Serializer.data
        print(ClassSchedule_data)
        class_schedule_list = list(filter(lambda x: str(week_count) in x['weeks'].split(','), ClassSchedule_data))

        res_json = {
            'code': 0,
            'msg': '成功',
            'week_day': int(week_day),
            'week_count': int(week_count),
            'data': class_schedule_list
        }
        return JsonResponse(res_json, json_dumps_params={'ensure_ascii': False})
