#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.clients.models import Client
from emma.apps.suscriptions.models import Suscription
from emma.apps.xauth.forms import UpdatePasswordForm
from emma.core.mixins import ClientRequiredMixin

import openpay


class ClientDetailView(ClientRequiredMixin, View):
    template_name = 'clients/client_detail.html'
    form_class = UpdatePasswordForm

    def get(self, request, **kwargs):
        form = self.form_class()
        ctx = {'form':form}
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        kwargs = {'request':request}
        form = self.form_class(request.POST, **kwargs)
        if form.is_valid():
            form.save()
            ctx = {'form': self.form_class(), 'success': 'La contraseña se actualizo correctamente'}
            return TemplateResponse(request, self.template_name, ctx)
        else:
            ctx = {'form': form}
            return TemplateResponse(request, self.template_name, ctx)


class AddCardView(ClientRequiredMixin, View):
    template_name = 'clients/add_card.html'

    def get(self, request, **kwargs):
        return TemplateResponse(request, self.template_name)

    def post(self, request):
        client = Client.objects.get(user=request.user)
        suscription = Suscription.objects.get(client=client)
        customer = openpay.Customer.retrieve(suscription.id_customer)

        card = customer.cards.create(
            token_id=request.POST['token_id'],
            device_session_id=request.POST['devsessionid']
        )
        return redirect(reverse_lazy('clients:dashboard_add_card'))