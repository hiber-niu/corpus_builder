#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from .views import HomePageView, RecordsListView, RelTypeView, RelTypeEditView, RelTypeAddView, download_file
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^reltype/(\d+)?/$', RelTypeView.as_view(), name='reltype'),
    url(r'^reltype/add/$', RelTypeAddView.as_view(), name='reltype_add'),
    url(r'^reltype/\d+/edit/$', RelTypeEditView.as_view(), name='reltype_edit'),

    url(r'^records/(\d+)?/$', RecordsListView.as_view(), name='records'),
    url(r'^download/(?P<file_name>.+)$', login_required(download_file)),
]
