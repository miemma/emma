#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/adult/(?P<id>.*)$',
        view=views.AdultInformation.as_view(),
        name='dashboard_adult'),

]
