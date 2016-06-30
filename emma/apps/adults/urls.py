#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/adulto/(?P<id>.*)$',
        view=views.AdultInformation.as_view(),
        name='dashboard_adult'),

]
