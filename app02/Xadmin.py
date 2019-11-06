#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: Xadmin.py

@time: 2019-11-05 10:07

@desc:

'''

from Xadmin.service.Xadmin import site,ModelXadmin
print('app02 Xadmin')

from app02.models import *

site.register(Order)
class FoodConfig(ModelXadmin):
    pass

site.register(Food,FoodConfig)
print('app02_registry',site._registry)