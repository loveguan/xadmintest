#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: Xadmin.py

@time: 2019-11-05 10:06

@desc:

'''
from Xadmin.service.Xadmin import site, ModelXadmin

print('app01 Xadmin')
from app01.models import *
from django.utils.safestring import mark_safe

# 继承自Modeladmin类，重写方法
class BookConfig(ModelXadmin):

    def edit(self,obj=None,is_header=False):
        if is_header:
            return "操作"
        return mark_safe("<a href='%s/change/'>编辑</a>" %obj.pk)

    def delete(self,obj=None,is_header=False):
        if is_header:
            return "操作"
        return mark_safe("<a href=''>删除</a>")

    def check(self,obj=None,is_header=False):
        if is_header:
            return "选择"
        return mark_safe("<input type='checkbox'>")

    list_display = [check, 'nid', 'title', 'publish', edit, delete]

site.register(Book, BookConfig)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)

print("_registry",site._registry)
