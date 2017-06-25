#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""corpus_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change, password_change_done
import nre

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r'^nre/', include('nre.urls')),

    url(r'^accounts/login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^password_change/$', password_change, {'template_name': 'registration/mypassword_change_form.html', 'post_change_redirect':'/password_change/done'}, name='password_change'),
    url(r'^password_change/done/$', password_change_done, {'template_name': 'registration/mypassword_change_done.html'}, name='password_change_done'),
]
