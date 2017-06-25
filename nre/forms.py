#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.forms import ModelForm
from .models import NERRelType


class NERRelTypeForm(ModelForm):
    class Meta:
        model = NERRelType
        fields = ['name',  'intro', 'status']
