#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: Xadmin.py

@time: 2019-11-05 9:41

@desc:

'''

from django.conf.urls import url, re_path
from django.shortcuts import HttpResponse, render, redirect


class ModelXadmin(object):
    list_display = ["__str__", ]

    def __init__(self, model, site):
        self.model = model
        self.site = site

    # 不重写默认的页面
    def list_view(self, request):
        # 获取model名称
        print("self.model", self.model)
        model_name = self.model._meta.model_name
        data_list = self.model.objects.all()
        print(data_list)
        print('list_display', self.list_display)

        # 处理表头数据
        head_list = []
        for field in self.list_display:
            if isinstance(field, str):
                if field=='__str__':
                    val=self.model._meta.model_name.upper()
                else:
                    field_obj=self.model._meta.get_field(field)
                    val=field_obj.verbose_name
            else:
                val = field(self, is_header=True)
            head_list.append(val)

        # 处理表单数据
        new_data_list = []
        for obj in data_list:
            temp = []
            for field in self.list_display:
                if isinstance(field, str):
                    val = getattr(obj, field)
                    print('1122123 %s' % val)
                else:
                    val = field(self, obj)
                temp.append(val)
            new_data_list.append(temp)
        print(new_data_list)
        return render(request, 'list_view.html', {"new_data_list": new_data_list, "model_name": model_name,"head_list":head_list })

    def add_view(self, request):

        return render(request, 'add_view.html')

    def change_view(self, request, id):

        return render(request, 'change_view.html')

    def delete_view(self, request, id):

        return render(request, 'delete_view.html')

    def get_url2(self):

        temp = []
        temp.append(url(r"^$", self.list_view))
        temp.append(url(r"^add/$", self.add_view))
        temp.append(url(r"^(\d+)/change/$", self.change_view))
        temp.append(url(r"^(\d+)/delete/$", self.delete_view))
        return temp

    @property
    def url2(self):

        return self.get_url2(), None, None


class XadminSite(object):

    def __init__(self, name='admin'):
        self._registry = {}

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelXadmin
        self._registry[model] = admin_class(model, self)

    def get_urls(self):
        temp = []
        print('*' * 20)
        print(self._registry)
        for model, admin_class_obj in self._registry.items():
            # 循环获取model的字符串和所在app的字符串
            app_name = model._meta.app_label
            model_name = model._meta.model_name
            temp.append(url(r'^{0}/{1}/'.format(app_name, model_name), admin_class_obj.url2), )
        return temp

    @property
    def urls(self):
        return self.get_urls(), None, None


site = XadminSite()
