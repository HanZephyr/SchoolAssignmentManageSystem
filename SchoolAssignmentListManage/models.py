# -*- coding: UTF-8 -*-
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 课程名
from django.forms import forms, ModelForm
from django.utils import timezone

from SchoolAssignmentListManage.diy_widgets import ImageInput, UploadModel


class ScheduleName(models.Model):
    # 科目名
    # schedule_name = models.CharField(max_length=50, choices=schedule_name_choice)
    schedule_name = models.CharField(max_length=50, verbose_name='课程名称', unique=True)

    class Meta:
        db_table = 'schedule_name'
        verbose_name = '课程'
        verbose_name_plural = "课程管理"

    def __str__(self):
        return self.schedule_name

class AssignmentInfo(models.Model):

    # 课程名
    schedule_name = models.ForeignKey(ScheduleName, on_delete=models.CASCADE, verbose_name='课程名称')

    # 作业信息
    assignmentInfo = models.CharField(verbose_name='作业内容', max_length=500)

    # 开始时间
    start_time = models.DateTimeField(verbose_name='开始时间', auto_now=False, default=timezone.now)
    # 结束时间
    end_time = models.DateTimeField(verbose_name='结束时间', auto_now=False, blank=True, null=True)

    # 补充信息
    additionalInfo = models.TextField(verbose_name='补充信息', blank=True, null=True, default=None)

    # 是否需要上传文件
    # is_need_upload_file = models.BooleanField(verbose_name='是否需要上传文件', default=False)

    # 文件
    upload_file = models.FileField(verbose_name='上传文件', blank=True, upload_to='..//static/uploadFile/',)

    # 图片
    # pic = models.ImageField(verbose_name='图片', blank=True, null=True, default=None)

    # images = forms.FileField(label="图片", widget=ImageInput, help_text="按住ctrl多选,最多4张", required=False)

    class Meta:
        # model = UploadModel
        verbose_name = '作业'
        verbose_name_plural = "作业管理"



