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
        name='contract_details'),

    url(regex='^contratar/emma/$',
        view=views.ContractEmmaPreference.as_view(),
        name='contract_emma'),

    url(regex='^contratar/pago/$',
        view=views.ContractPay.as_view(),
        name='contract_payment'),

    url(regex='^contratar/comprobacion/$',
        view=views.ContractComprobation.as_view(),
        name='contract_comprobation'),


]
