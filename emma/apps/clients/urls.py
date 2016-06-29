#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/cliente/$',
        view=views.ClientDetailView.as_view(),
        name='dashboard_client_detail'),

    url(regex='^dashboard/tarjeta/$',
        view=views.AddCardView.as_view(),
        name='dashboard_add_card'),
]