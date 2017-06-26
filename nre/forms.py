#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from django.forms import ModelForm
from .models import NERRelType


class NERRelTypeForm(ModelForm):
    class Meta:
        model = NERRelType
        fields = ['name',  'intro', 'status']


class RecordUploadForm(forms.Form):
    split_tag = forms.CharField(label="字段分隔符")
    source = forms.CharField(label="数据来源")
    upload_file = forms.FileField()
    fields_layout = [('split_tag', 'source',), upload_file,]
