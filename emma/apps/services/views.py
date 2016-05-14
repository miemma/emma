#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class ContractServiceInfo(TemplateView):
    template_name = 'services/contract_service_info.html'