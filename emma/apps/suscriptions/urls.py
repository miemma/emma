#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^dashboard/historial-pagos/$',
        view=views.ChargesList.as_view(),
        name='dashboard_charges_list'),

    url(regex=r'^dashboard/historial/$',
        view=views.HistoryList.as_view(),
        name='dashboard_history_list'),

    url(regex=r'^dashboard/informacion-pago/$',
        view=views.PaymentInfo.as_view(),
        name='dashboard_payment_info'),
]