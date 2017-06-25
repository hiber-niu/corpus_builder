#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import date, datetime, timedelta


class NERRelType(models.Model):
    STATUS_DEFAULT = 0
    STATUS_DISABLE = 1
    STATUS_AVAILABLE = 2
    STATUS_CHOICES = (
        (STATUS_DEFAULT, '默认'),
        (STATUS_DISABLE, '禁用'),
        (STATUS_AVAILABLE, '可用')
    )
    name = models.CharField(max_length=100, verbose_name='关系名称', unique=True)
    intro = models.TextField(default='', blank=True, verbose_name='简介')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    status = models.IntegerField(default=STATUS_DEFAULT, choices=STATUS_CHOICES, verbose_name="状态")

    all_count = models.IntegerField(default=0, blank=True, verbose_name='样本数目')
    pos_count = models.IntegerField(default=0, blank=True, verbose_name='正例数目')
    neg_count = models.IntegerField(default=0, blank=True, verbose_name='反例数目')
    zero_count = models.IntegerField(default=0, blank=True, verbose_name='未标数目')

    def get_all_count(self):
        return Record.objects.filter(rel_type=self).count()

    def get_pos_count(self):
        return Record.objects.filter(rel_type=self).filter(tag=1).count()

    def get_neg_count(self):
        return Record.objects.filter(rel_type=self).filter(tag=-1).count()

    def get_zero_count(self):
        return Record.objects.filter(rel_type=self).filter(tag=0).count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "关系类型"


class Record(models.Model):
    TAG_DEFAULT = 0
    TAG_POS = 1
    TAG_NEG = -1
    TAG_CHOICES = (
        (TAG_DEFAULT, '默认'),
        (TAG_POS, '正例'),
        (TAG_NEG, '反例')
    )

    rel_type = models.ForeignKey('NERRelType', verbose_name='所属类型')
    unique_id = models.CharField(max_length=500, default='', verbose_name='记录标识')
    spans = models.CharField(max_length=500, default='', verbose_name='span')
    content = models.TextField(default='', verbose_name='文本内容')
    tag = models.IntegerField(default=TAG_DEFAULT, choices=TAG_CHOICES, verbose_name="标注结果")
    source = models.CharField(max_length=500, default='', verbose_name='来源')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = "样本实例"
