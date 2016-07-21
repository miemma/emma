#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpay
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import ListView, View

from emma.apps.adults.models import AdultAddress, Adult
from emma.apps.services.models import HiredService
from emma.apps.suscriptions.models import Charge, Suscription, History
from emma.core.mixins import ClientRequiredMixin, GetAdultMixin


class ChargesList(GetAdultMixin, ClientRequiredMixin, ListView):
    template_name = 'suscriptions/charges_list.html'
    model = Charge
    context_object_name = 'charges'

    def get_queryset(self):
        suscription = Suscription.objects.get(client=self.request.user.client)
        queryset = Charge.objects.filter(suscription=suscription)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ChargesList, self).get_context_data(**kwargs)
        context['adult'] = self.get_adult(self.request)
        return context


class HistoryList(GetAdultMixin, ClientRequiredMixin, ListView):
    template_name = 'suscriptions/history_list.html'
    model = History
    context_object_name = 'histories'

    def get_queryset(self):
        suscription = Suscription.objects.get(client=self.request.user.client)
        queryset = self.model.objects.filter(suscription=suscription)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HistoryList, self).get_context_data(**kwargs)
        context['adult'] = self.get_adult(self.request)
        return context


class PaymentInfo(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'suscriptions/payment_info.html'

    def get(self, request):
        suscription = Suscription.objects.get(client=self.request.user.client)
        customer = openpay.Customer.retrieve(suscription.openpay_id)
        cards = customer.cards.all()

        ctx = {
            'cards': cards.data,
            'adult': self.get_adult(request)
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post (self, request):
        suscription = Suscription.objects.get(client=request.user.client)
        customer = openpay.Customer.retrieve(suscription.openpay_id)
        try:
            card = customer.cards.retrieve(request.POST['card_id'])
        except:
            card = None
        if card is not None:
            card.delete()
        return redirect(reverse_lazy('suscriptions:dashboard_payment_info'))


class SuscriptionDetail(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'suscriptions/dashboard_suscription.html'

    def get(self, request):
        service = HiredService.objects.get(
            client=self.request.user.client
        )

        adult = Adult.objects.get(responsable=self.request.user.client)

        address = AdultAddress.objects.get(
            adult=adult)

        ctx = {
            'adult': self.get_adult(request),
            'name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
            'service': service.service.name,
            'workshops': service.workshops,
            'days': service.service_days,
            'street': address.street,
            'outdoor_number': address.outdoor_number,
            'colony': address.colony,
            'municipality': address.municipality,
            'postal_code': address.postal_code,
            'city': address.city,
            'state': address.state,
            'reference': address.reference,
            'adult_first_name': adult.first_name,
            'adult_last_name': adult.last_name,
            'age': adult.birthday,
            'emma_principal': service.emma_assigned,
            'emma_secundary': service.emma_alternate,
            'emma_cordinator': service.emma_cordinator,
        }
        return TemplateResponse(request, self.template_name, ctx)