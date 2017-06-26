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
    template_name = 'nre/records.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        if len(self.args) > 0 and self.args[0] != None:
            table = RecordTable(Record.objects.filter(rel_type=self.args[0]).order_by('-id'))
            table.paginate(page=request.GET.get('page', 1), per_page=50)
            context['records'] = table
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.POST.get("submit") and request.FILES['corpus_file']:
            corpus_file = request.FILES['corpus_file']

            filename = fs.save(corpus_file.name, corpus_file)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })

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



"""
@login_required
def index(request):
    context = {}
    params = request.GET.copy()
    status = params.get('status', None)
    _obj_list = NERRelType.objects.filter().order_by('-id')

    paginator = Paginator(_obj_list, 50)  # Show 20 contacts per page

    page = request.GET.get('page')
    try:
        _objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        _objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        _objs = paginator.page(paginator.num_pages)

    context.update({
        "active_nav": "wechats",
        "wechats": _objs,
        "params": params,
        "downloader": r.llen(CRAWLER_CONFIG['downloader']) or 0,
        "antispider": r.get(CRAWLER_CONFIG['antispider']) or 0,
        "proxy_status": _proxy_status

    })

    return render_to_response('nre/index.html', RequestContext(request, context))
"""
