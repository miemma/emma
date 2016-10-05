#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/emma-titular/$',
        view=views.MainEmmaView.as_view(),
        name='dashboard_main_emma'),

    url(regex='^dashboard/emma-alternativa/$',
        view=views.SecondEmmaView.as_view(),
        name='dashboard_alternative_emma'),

    url(regex='^dashboard/emma-coordinadora/$',
        view=views.CoordinatorEmmaView.as_view(),
        name='dashboard_coordinator_emma'),

    url(regex='^dashboard/emma-pendiente/$',
        view=views.StandEmma.as_view(),
        name='dashboard_standby_emma'),
]