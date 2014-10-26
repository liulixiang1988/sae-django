# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='home'),
                       url(r'^add_bill/$', views.add_bill, name='add_bill'),
                       )
