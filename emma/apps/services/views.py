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
from emma.apps.clients.models import Client
from emma.apps.services.forms import ServiceData, ContractAdultInfo
from emma.apps.services.models import Service, Workshop, HiredService
from emma.apps.suscriptions.models import Suscription, History
from emma.core.mixins import RequestFormMixin, ActiveClientRequiredMixin

from datetime import datetime, date

from emma.core.utils import send_email


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


class ContractAdult(ActiveClientRequiredMixin, RequestFormMixin, FormView):
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


class ContractComprobation(ActiveClientRequiredMixin, View):
    template_name = 'services/contract_confirmation.html'

    def get(self, request, **kwargs):
        if not 'adult_setup' in request.session:
            return redirect('services:contract_adult')
        service = HiredService.objects.get(
            client=self.request.user.client
        )

        address = AdultAddress.objects.get(user=self.request.user)

        adult = Adult.objects.get(responsable=self.request.user.client)

        doctor = Doctor.objects.get(adult=adult)

        def calculate_age(born):
            today = date.today()
            try:
                birthday = born.replace(year=today.year)
            except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
                birthday = born.replace(year=today.year, day=born.day - 1)
            if birthday > today:
                return today.year - born.year - 1
            else:
                return today.year - born.year

        day, month, year = [int(x) for x in adult.birthday.split("/")]
        born = date(year, month, day)

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
            'day_1': service.service_day_1,
            'day_2': service.service_day_2,
            'day_3': service.service_day_3,
            'day_4': service.service_day_4,
            'day_5': service.service_day_5,
            'day_6': service.service_day_6,
            'day_7': service.service_day_7,
            'adult_first_name': adult.first_name,
            'adult_last_name': adult.last_name,
            'adult_phone': adult.phone,
            'adult_emergency': adult.emergency_phone,
            'age': calculate_age(born),
            'doctor_name': doctor.name,
            'doctor_phone': doctor.phone,
        }

        return TemplateResponse(request, self.template_name, ctx)


class ContractPay(ActiveClientRequiredMixin, View):
    template_name = 'services/contract_payment.html'

    def get(self, request):
        if not 'service_setup' in request.session:
            return redirect('services:contract_ubication')
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

        del request.session['adult_setup']
        del request.session['days_per_service']
        del request.session['id_service']
        del request.session['workshop_list']

        return redirect(reverse_lazy('landing:success_contract'))


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