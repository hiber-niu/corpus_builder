#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import mimetypes
import os

from django.utils.encoding import smart_str

from .models import *
from .tables import *
from .forms import *


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'nre/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        table = NERRelTypeTable(NERRelType.objects.filter().order_by('-id'))
        table.paginate(page=request.GET.get('page', 1), per_page=20)
        context['reltypes'] = table
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


class RecordsListView(LoginRequiredMixin, TemplateView):
    template_name = 'nre/record.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        if len(self.args) > 0 and self.args[0] != None:
            table = RecordTable(Record.objects.filter(rel_type=self.args[0]).order_by('-id'))
            table.paginate(page=request.GET.get('page', 1), per_page=50)
            context['records'] = table
            form = RecordUploadForm()
            context['form'] = form
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if 'upload' in request.POST and request.FILES['corpus_file']:
            if len(self.args) > 0 and self.args[0] != None:
                corpus_file = request.FILES['corpus_file']

                fs = FileSystemStorage()
                filename = fs.save(corpus_file.name, corpus_file)
                context['filename'] = filename
                messages.success(request, '文件上传成功！')
                messages.info(request, '正在录入文件，请稍候......')

                file_path = settings.MEDIA_ROOT + '/' + file_name
                with open(file_path, 'rb') as f:
                    for line in f.readlines():
                        line.split('||')






            return render(request, self.template_name, context)


class RelTypeView(LoginRequiredMixin, TemplateView):
    template_name = 'nre/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        table = NERRelTypeTable(NERRelType.objects.filter().order_by('-id'))
        table.paginate(page=request.GET.get('page', 1), per_page=20)
        context['reltypes'] = table
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


class RelTypeAddView(LoginRequiredMixin, TemplateView):
    template_name = 'nre/add.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        form = NERRelTypeForm()
        context['reltype_form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        post_form = NERRelTypeForm(request.POST or None)
        if "add" in request.POST:
            if post_form.is_valid():
                post_form.save()
                messages.add_message(request, messages.SUCCESS, u'关系录入成功！')
                return HttpResponseRedirect('/nre/')
            return render_to_response(self.template_name, {'reltype_form': post_form})


class RelTypeEditView(LoginRequiredMixin, TemplateView):
    template_name = 'nre/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        if len(self.args) > 0 and self.args[0] != None:
            rel = NERRelType.objects.get(id=self.args[0])
            form = NERRelTypeForm(instance=rel)
            context['rel_form'] = form
            context['id'] = upfile.id

        table = NERRelTypeTable(NERRelType.objects.filter().order_by('-id'))
        table.paginate(page=request.GET.get('page', 1), per_page=20)
        context['reltypes'] = table
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


def download_file(request, file_name):
    file_path = settings.MEDIA_ROOT + '/' + file_name
    # file_wrapper = FileWrapper(open(file_path, 'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=file_mimetype[0])
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
            return response
    else:
        return HttpResponseNotFound()
