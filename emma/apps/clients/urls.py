#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/cliente/$',
        view=views.ClientDetailView.as_view(),
        name='dashboard_client_detail'),

    url(regex='^dashboard/tarjeta/$',
        view=views.PayCardView.as_view(),
        name='dashboard_add_card'),

    url(regex='^dashboard/bienvenida/$',
        view=views.WelcomeView.as_view(),
        name='dashboard_welcome'),

]