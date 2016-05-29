#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View, FormView

from emma.apps.services.forms import ServiceData, ContractAdultInfo
from emma.apps.services.models import Service, Workshop, HiredService
from emma.apps.users.models import Address
from emma.core.mixins import RequestFormMixin, ActiveClientRequiredMixin


class ContractServiceInfo(ActiveClientRequiredMixin, View):
    template_name = 'services/contract_service_info.html'
    services = Service.objects.all()
    success_url = reverse_lazy('services:contract_location')

    def get(self, request, **kwargs):
        ctx = {
            'services': self.services
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        service_id = request.POST.get('contract-service')
        workshop_list = request.POST.getlist('contract-service-workshop')
        ctx = {
            'services': self.services
        }
        try:
            service = self.services.get(id=service_id)
            for workshop in workshop_list:
                Workshop.objects.get(id=workshop, service=service)
            request.session['id_service'] = service_id
            request.session['workshop_list'] = workshop_list
            return redirect(self.success_url)

        except Service.DoesNotExist:
            error = 'Ocurrio un error, intente de nuevo'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)
        except Workshop.DoesNotExist:
            error = 'Ocurrio un error, intente de nuevo'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)


class ContractLocation(ActiveClientRequiredMixin, RequestFormMixin, FormView):
    template_name = 'services/contract_location.html'
    form_class = ServiceData
    success_url = reverse_lazy('services:contract_adult')

    def get(self, request, **kwargs):
        if not 'days_per_service' in request.session:
            request.session['days_per_service'] = 1
        return super(ContractLocation, self).get(self, request, **kwargs)

    def form_valid(self, form):
        form.save()
        self.request.session['service_setup'] = True
        return super(ContractLocation, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContractLocation, self).get_context_data(**kwargs)
        service = Service.objects.get(
            id=self.request.session['id_service']
        )
        workshop_list = self.request.session['workshop_list']
        workshops = []
        for workshop in workshop_list:
            work = Workshop.objects.get(id=workshop, service=service)
            workshops.append(work)
        context['service'] = service
        context['workshops'] = workshops
        return context


class ContractAdult(RequestFormMixin, FormView):
    template_name = 'services/contract_adult.html'
    form_class = ContractAdultInfo
    success_url = reverse_lazy('services:contract_comprobation')

    def get(self, request, **kwargs):
        if not 'service_setup' in request.session:
            return redirect('services:contract_ubication')
        return super(ContractAdult, self).get(self, request, **kwargs)

    def form_valid(self, form):
        form.save()
        self.request.session['adult_setup'] = True
        return super(ContractAdult, self).form_valid(form)


class ContractComprobation(View):
    template_name = 'services/contract_confirmation.html'

    def get(self, request, **kwargs):
        # if not 'adult_setup' in request.session:
            # return redirect('services:contract_adult')

        service = HiredService.objects.filter(
            client=self.request.user.client
        )[0]


        address = Address.objects.filter(user=self.request.user)[0]

        ctx = {
            'name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'service': service.service.name,
            'workshops': service.workshops,
            'street': address.street,
            'outdoor_number': address.outdoor_number,
            'colony': address.colony,
            'municipality': address.municipality,
            'postal_code': address.postal_code,
            'city': address.city,
            'state': address.state,
            'reference': address.reference,


        }
        return TemplateResponse(request, self.template_name, ctx)


class ContractPay(TemplateView):
    template_name = 'services/contract_payment.html'


class ContractAddDay(View):
    @staticmethod
    def get(request):
        raise Http404("Page not found")

    @staticmethod
    def post(request):
        request.session['days_per_service'] +=1
        return HttpResponse('Add Day')


class ContractRemoveDay(View):
    @staticmethod
    def get(request):
        raise Http404("Page not found")

    @staticmethod
    def post(request):
        request.session['days_per_service'] -=1
        # del request.session['days_per_service']
        return HttpResponse('Remove Day')