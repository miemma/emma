#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import ListView

from emma.apps.suscriptions.models import Charge, Suscription
from emma.core.mixins import ClientRequiredMixin


class ChargesList(ClientRequiredMixin, ListView):
    template_name = 'suscriptions/charges_list.html'
    model = Charge
    context_object_name = 'charges'

    def get_queryset(self):
        suscription = Suscription.objects.get(client=self.request.user.client)
        queryset = Charge.objects.filter(suscription=suscription)
        return queryset