# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NERRelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='关系名称')),
                ('intro', models.TextField(blank=True, default='', verbose_name='简介')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('status', models.IntegerField(choices=[(0, '默认'), (1, '禁用'), (2, '可用')], default=0, verbose_name='状态')),
                ('all_count', models.IntegerField(blank=True, default=0, verbose_name='样本数目')),
                ('pos_count', models.IntegerField(blank=True, default=0, verbose_name='正例数目')),
                ('neg_count', models.IntegerField(blank=True, default=0, verbose_name='反例数目')),
                ('zero_count', models.IntegerField(blank=True, default=0, verbose_name='未标数目')),
            ],
            options={
                'verbose_name_plural': '关系类型',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default='', max_length=500, verbose_name='记录标识')),
                ('spans', models.CharField(default='', max_length=500, verbose_name='span')),
                ('content', models.TextField(default='', verbose_name='文本内容')),
                ('tag', models.IntegerField(choices=[(0, '默认'), (1, '正例'), (-1, '反例')], default=0, verbose_name='标注结果')),
                ('source', models.CharField(default='', max_length=500, verbose_name='来源')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('rel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nre.NERRelType', verbose_name='所属类型')),
            ],
            options={
                'verbose_name_plural': '样本实例',
            },
        ),
    ]
