#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_title,name='blog_title'),
    url(r'(?P<article_id>\d)/$',views.blog_details,name='blog_detail'),
]