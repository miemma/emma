#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^contratar/informacion-servicio/$',
        view=views.ContractServiceInfo.as_view(),
        name='contract_service_info'),

    url(regex='^contratar/registro/$',
        view=views.ContractSignup.as_view(),
        name='contract_signup'),

    url(regex='^contratar/ubicacion/$',
        view=views.ContractLocation.as_view(),
        name='contract_ubication'),

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
