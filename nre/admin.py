#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
"""
from django.core import urlresolvers
from .models import *


class NERRelTypeAdmin(admin.ModelAdmin):
    fields = (('name', 'status'),)
    list_display = ('id', 'name', 'all_count', 'pos_count', 'neg_count',
                    'zero_count', 'update_time', 'status', 'link_to_record')
    search_fields = ['name']

    def link_to_record(self, obj):
        link = urlresolvers.reverse('admin:nre_record_change', args=[obj.id])
        return '<a href="%s">%s</a>' % (link, obj.Record.name)
    link_to_record.allow_tags = True


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'rel_type', 'content', 'tag', 'source', 'update_time')

admin.site.register(NERRelType, NERRelTypeAdmin)
"""
