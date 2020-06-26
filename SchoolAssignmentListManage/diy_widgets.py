# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/12 20:51
# @Author: 韩家旭
# @File  : diy_widgets.py.py

from django.forms import ClearableFileInput, ModelForm, forms
from django.template import loader
from django.utils.safestring import mark_safe
from django.db import models


class ImageInput(ClearableFileInput):
    template_name = 'image_multi_upload.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class UploadModel(models.Model):
    images = models.FileField('图片', upload_to="static/Assignment/UploadImg")


class UploadForm(ModelForm):
    images = forms.FileField(label="图片", widget=ImageInput, help_text="按住ctrl多选,最多4张", required=False)

    class Meta:
        model = UploadModel
        fields = ['images']


