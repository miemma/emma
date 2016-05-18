#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^usuarios/historial-pagos', view=views.ChargesList.as_view(),
        name='select_card'),
]