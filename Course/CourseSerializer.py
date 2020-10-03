# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/10/3 16:32
# @Author: 韩家旭
# @File  : CourseSerializer.py

from rest_framework import serializers
from rest_framework.utils.field_mapping import get_nested_relation_kwargs
from datetime import time
from .models import ClassSchedule


class CourseSerializer(serializers.ModelSerializer):

    def build_nested_field(self, field_name, relation_info, nested_depth):
        """
        Create nested fields for forward and reverse relationships.
        """

        class NestedSerializer(serializers.ModelSerializer):
            class Meta:
                model = relation_info.related_model
                depth = nested_depth - 1
                fields = '__all__'
                extra_kwargs = self.get_extra_kwargs()

        field_class = NestedSerializer
        field_kwargs = get_nested_relation_kwargs(relation_info)

        return field_class, field_kwargs

    @staticmethod
    def get_time_interval(obj):
        start_time = obj.lesson.start_time
        end_time = obj.lesson.end_time
        midday_time = time(12, 0, 0)
        if start_time.__lt__(midday_time):
            return '上午'
        else:
            return '下午'

    time_interval = serializers.SerializerMethodField()

    class Meta:
        model = ClassSchedule
        fields = '__all__'
        depth = 2
        extra_kwargs = {
            'start_time': {'format': '%H:%M'},
            'end_time': {'format': '%H:%M'}
        }
