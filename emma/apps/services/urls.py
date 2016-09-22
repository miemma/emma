#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^contratar/plan/$',
        view=views.ContractPlan.as_view(),
        name='contract_plan'),

    url(regex='^contratar/detalles/$',
        view=views.ContractPlanDetails.as_view(),
        name='contract_plan'),

    url(regex='^contratar/ubicacion/$',
        view=views.ContractLocation.as_view(),
        name='contract_location'),

    url(regex='^contratar/adulto/$',
        view=views.ContractAdult.as_view(),
        name='contract_adult'),

    url(regex='^contratar/comprobacion/$',
        view=views.ContractComprobation.as_view(),
        name='contract_comprobation'),

    url(regex='^contratar/pago/$',
        view=views.ContractPay.as_view(),
        name='contract_payment'),

    url(regex='^contratar/agregar-dia/$',
        view=views.ContractAddDay.as_view(),
        name='contract_add_day'),

    url(regex='^contratar/remover-dia/$',
        view=views.ContractRemoveDay.as_view(),
        name='contract_remove_day'),

]
