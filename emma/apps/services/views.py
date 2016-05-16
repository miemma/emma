#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, FormView

from emma.apps.xauth.views import SignupView


class ContractServiceInfo(TemplateView):
    template_name = 'services/contract_service_info.html'


class ContractSignup(SignupView):
    template_name = 'services/contract_signup.html'


class ContractLocation(TemplateView):
    template_name = 'services/contract_location.html'


class ContractAdult(TemplateView):
    template_name = 'services/contract_adult.html'

class ContractPay(TemplateView):
    template_name = 'services/contract_payment.html'
