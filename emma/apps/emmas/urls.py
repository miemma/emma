#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^dashboard/emma-titular/$',
        view=views.MainEmma.as_view(),
        name='dashboard_main_emma'),

]