#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^usuarios/historial-pagos/$',
        view=views.ChargesList.as_view(),
        name='charges_list'),

    url(regex=r'^usuarios/historial/$',
        view=views.HistoryList.as_view(),
        name='history_list'),
]