#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^agregar-tarjeta/', view=views.AddCardView.as_view(),
        name='add_card'),

    url(regex=r'^pagar-servicio/', view=views.SelectCardView.as_view(),
        name='select_card'),

]