#!/usr/bin/env python
# -*- coding: utf-8 -*-


import django_tables2 as tables
from django_tables2.utils import A
from .models import *


class NERRelTypeTable(tables.Table):
    name = tables.LinkColumn('records', text=lambda record: record.name, args=[A('id')])
    records = tables.LinkColumn('records', text='查看语料', args=[A('id')], verbose_name='关联语料')

    class Meta:
        model = NERRelType
        attrs = {'class': 'table table-responsive'}
        # add class="paleblue" to <table> tag


class RecordTable(talbes.Table):
    class Meta:
        model = Record
        attrs = {'class': 'table table-responsive'}
