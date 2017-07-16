#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/bienvenida/admin$',
        view=views.WelcomeView.as_view(),
        name='dashboard_welcome'),

]