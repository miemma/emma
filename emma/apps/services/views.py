#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View

from emma.apps.services.models import Service, Workshop
from emma.apps.xauth.views import SignupView


class ContractServiceInfo(View):
    template_name = 'services/contract_service_info.html'
    services = Service.objects.all()
    success_url = reverse_lazy('services:contract_signup')

    def get(self, request):
        ctx = {
            'services': self.services
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        service_id = request.POST.get('contract-service')
        workshop_id = request.POST.get('contract-service-workshop')
        ctx = {
            'services': self.services
        }
        try:
            service = self.services.get(id=service_id)
            Workshop.objects.get(id=workshop_id, service=service)
            request.session['id_service'] = service_id
            request.session['id_workshop'] = workshop_id
            return redirect(self.success_url)

        except Service.DoesNotExist:
            error = 'No se encontro el servicio deseado'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)
        except Workshop.DoesNotExist:
            error = 'No se encontro el taller deseado'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)


class ContractSignup(SignupView):
    template_name = 'services/contract_signup.html'
    success_url = reverse_lazy('services:contract_ubication')

    def get(self, request, **kwargs):
        if not 'id_service' in request.session or \
                not 'id_workshop' in request.session :
            return redirect('services:contract_service_info')
        else:
            return super(ContractSignup, self).get(self, request, **kwargs)


class ContractLocation(TemplateView):
    template_name = 'services/contract_location.html'


class ContractAdult(TemplateView):
    template_name = 'services/contract_adult.html'

class ContractPay(TemplateView):
    template_name = 'services/contract_payment.html'
