#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpay
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import View, FormView

from emma.apps.adults.models import Adult, AdultAddress
from emma.apps.doctors.models import Doctor
from emma.apps.clients.models import Client, ContractProcess
from emma.apps.services.forms import ServiceData, ContractAdultInfo
from emma.apps.services.models import Service, Workshop, HiredService
from emma.apps.suscriptions.models import Suscription, History
from emma.core.mixins import RequestFormMixin, ActiveClientRequiredMixin

from datetime import datetime, date


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
        id_service = request.POST.get('contract-service')
        workshop_list = request.POST.getlist('contract-service-workshop')
        ctx = {
            'services': self.services
        }
        try:
            service = self.services.get(id=id_service)
            for workshop in workshop_list:
                Workshop.objects.get(id=workshop, service=service)
            try:
                contract_process = ContractProcess.objects.get(
                    client=request.user.client
                )
                contract_process.id_service = id_service
                contract_process.workshop_list = workshop_list
            except ContractProcess.DoesNotExist:
                contract_process = ContractProcess(
                    client=request.user.client,
                    id_service=id_service,
                    workshop_list=workshop_list
                )
            contract_process.save()
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
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        if not contract_process.id_service or not contract_process.workshop_list:
            return redirect(reverse_lazy('services:contract_service_info'))
        if not contract_process.service_days:
            contract_process.service_days = 1
            contract_process.save()
        return super(ContractLocation, self).get(self, request, **kwargs)

    def form_valid(self, form):
        form.save()
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        contract_process.service_setup = True
        contract_process.save()
        return super(ContractLocation, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContractLocation, self).get_context_data(**kwargs)
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        service = Service.objects.get(
            id=contract_process.id_service
        )
        workshop_list = []
        for x in contract_process.workshop_list:
            if x.isdigit():
                workshop_list.append(x)
        workshops = []
        for workshop in workshop_list:
            work = Workshop.objects.get(id=workshop, service=service)
            workshops.append(work)
        context['service'] = service
        context['workshops'] = workshops
        context['days'] = contract_process.service_days
        return context


class ContractAdult(ActiveClientRequiredMixin, RequestFormMixin, FormView):
    template_name = 'services/contract_adult.html'
    form_class = ContractAdultInfo
    success_url = reverse_lazy('services:contract_comprobation')

    def get(self, request, **kwargs):
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        if contract_process.service_setup is not True:
            return redirect(reverse_lazy('services:contract_location'))
        return super(ContractAdult, self).get(self, request, **kwargs)

    def form_valid(self, form):
        form.save()
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        contract_process.adult_setup = True
        contract_process.save()
        return super(ContractAdult, self).form_valid(form)


class ContractComprobation(ActiveClientRequiredMixin, View):
    template_name = 'services/contract_confirmation.html'

    def get(self, request, **kwargs):
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        if contract_process.adult_setup is not True:
            return redirect('services:contract_adult')

        service = HiredService.objects.get(
            client=self.request.user.client
        )

        address = AdultAddress.objects.get(id=contract_process.adult_address_id)

        adult = Adult.objects.get(responsable=self.request.user.client)

        ctx = {
            'name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
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
            'day_1': service.service_days.service_day_1,
            'day_2': service.service_days.service_day_2,
            'day_3': service.service_days.service_day_3,
            'day_4': service.service_days.service_day_4,
            'day_5': service.service_days.service_day_5,
            'day_6': service.service_days.service_day_6,
            'day_7': service.service_days.service_day_7,
            'adult_first_name': adult.first_name,
            'adult_last_name': adult.last_name,
            'age': adult.birthday,
        }

        return TemplateResponse(request, self.template_name, ctx)


class ContractPay(ActiveClientRequiredMixin, View):
    template_name = 'services/contract_payment.html'

    def get(self, request):
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        if contract_process.adult_setup is not True:
            return redirect('services:contract_adult')
        return render(request, self.template_name)

    def post(self, request):
        client = Client.objects.get(user=request.user)

        customer = openpay.Customer.create(
            name=request.user.get_full_name(),
            email=request.user.email,
            requires_account=False,
            status='active',
        )

        suscription = Suscription(
            client=client,
            id_customer=customer.id,
            status='active',
            is_active=True,
            date=datetime.today()
        )

        suscription.save()

        history = History(
            suscription=suscription,
            movement="Suscripcion Creada"
        )
        history.save()

        card = customer.cards.create(
            token_id=request.POST['token_id'],
            device_session_id=request.POST['devsessionid']
        )

        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        ).delete()

        return redirect(reverse_lazy('landing:success_contract'))


class ContractAddDay(View):
    @staticmethod
    def get(request):
        raise Http404("Page not found")

    @staticmethod
    def post(request):
        contract_process = ContractProcess.objects.get(
            client=request.user.client
        )
        contract_process.service_days +=1
        contract_process.save()
        return HttpResponse('Add Day')


class ContractRemoveDay(View):
    @staticmethod
    def get(request):
        raise Http404("Page not found")

    @staticmethod
    def post(request):
        contract_process = ContractProcess.objects.get(
            client=request.user.client
        )
        contract_process.service_days -= 1
        contract_process.save()
        return HttpResponse('Remove Day')