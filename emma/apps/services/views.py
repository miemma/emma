#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpay

from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.models import Adult
from emma.apps.clients.models import Client
from emma.apps.services.models import Service, Workshop, \
    ServiceDay, Activity, HiredService, UniqueService
from emma.apps.suscriptions.models import Suscription, Charge
from emma.core.mixins import ActiveClientRequiredMixin

from datetime import datetime


class ContractPlan(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('services:contract_details')

    @staticmethod
    def get_context(request):
        plans = Service.objects.all()
        ctx = {
            'plans': plans
        }
        return ctx

    def get(self, request):
        ctx = self.get_context(request)
        return TemplateResponse(request, 'services/contract_plan.html', ctx)

    def post(self, request):
        plan = Service.objects.get(id=request.POST.get('plan'))
        try:
            HiredService.objects.get(
                client=request.user.client
            ).delete()
        except HiredService.DoesNotExist:
            pass

        service = HiredService(
            client=request.user.client,
            service=plan,
        )
        service.save()
        return redirect(self.success_url)


class ContractPlanDetails(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('services:contract_emma')
    @staticmethod
    def get_context(request):
        workshops = Workshop.objects.all()
        activities = Activity.objects.all()
        service = HiredService.objects.get(
            client=request.user.client,
        )
        weekly_sessions = range(1, service.service.max_weekly_sessions + 1)
        weekly_hours = range(1, service.service.weekly_hours + 1)
        ctx = {
            'workshops': workshops,
            'activities': activities,
            'service': service,
            'weekly_sessions': weekly_sessions,
            'weekly_hours': weekly_hours
        }
        return ctx

    def get(self, request):
        ctx = self.get_context(request)
        contract_process = HiredService.objects.get(client=request.user.client)
        days = ServiceDay.objects.filter(service=contract_process)
        for x in days:
            x.delete()
        return TemplateResponse(request, 'services/contract_details.html', ctx)

    def post(self, request):
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        contract_process = HiredService.objects.get(client=request.user.client)
        for x in days:
            if request.POST.get('%s_day' % x):
                # """
                workshop_activity = request.POST.get('%s_workshop_activity' % x).split('-')
                try:
                    content = Workshop.objects.get(id=workshop_activity[0], name=workshop_activity[1])
                except Workshop.DoesNotExist:
                    try:
                        content = Activity.objects.get(id=workshop_activity[0], name=workshop_activity[1])
                    except Activity.DoesNotExist:
                        raise Http404
                # """
                service_day = ServiceDay(
                    service=contract_process,
                    day=request.POST.get('%s_day' % x),
                    start_time=request.POST.get('%s_start_time' % x),
                    duration=request.POST.get('%s_weekly_sessions' % x),
                    #duration=1,
                    content_object=content
                )
                service_day.save()
        return redirect(self.success_url)


class ContractEmmaPreference(ActiveClientRequiredMixin, View):
    succes_url = reverse_lazy('services:contract_payment')
    def get(self, request, **kwargs):
        return TemplateResponse(request, 'services/contract_emma.html')
    def post(self, request, **kwargs):
        contract_process = HiredService.objects.get(client=request.user.client)
        gender = request.POST.get('gender')
        contract_process.emma_type = gender
        languages = request.POST.getlist('language')
        str_languages = ""
        for language in languages:
            str_languages += '%s, ' % str(language)
        str_languages = str_languages[:-2]
        contract_process.languages = str_languages
        knowledges = request.POST.getlist('knowledge')
        str_knowledges = ""
        for knowledge in knowledges:
            str_knowledges += '%s, ' % str(knowledge)
        str_knowledges = str_knowledges[:-2]
        contract_process.knowledges = str_knowledges
        skills = request.POST.getlist('skill')
        str_skills = ""
        for skill in skills:
            str_skills += '%s, ' % str(skill)
        str_skills = str_skills[:-2]
        contract_process.skills = str_skills
        certifications = request.POST.getlist('certification')
        str_certifications = ""
        for cartification in certifications:
            str_certifications += '%s, ' % str(cartification)
        str_certifications = str_certifications[:-2]
        contract_process.certifications = str_certifications
        contract_process.save()
        return redirect(self.succes_url)


class ContractPay(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('services:contract_comprobation')
    def get(self, request):
        return render(request, 'services/contract_pay.html')

    def post(self, request):
        client = Client.objects.get(user=request.user)
        contract_service = HiredService.objects.get(
            client=client)

        customer = openpay.Customer.create(
            name=request.user.get_full_name(),
            email=request.user.email,
            requires_account=False,
            status='active',
        )

        suscription = Suscription(
            client=client,
            openpay_id=customer.id,
            status='active',
            is_active=True,
            date=datetime.today()
        )

        suscription.save()

        card = customer.cards.create(
            token_id=request.POST['token_id'],
            device_session_id=request.POST['devsessionid']
        )

        try:
            charge = openpay.Charge.create(
                source_id=card.id,
                method="card",
                amount=contract_service.service.price,
                currency="MXN",
                description="Cargo por plan %s de emma" % contract_service.service.name,
                customer=customer.id,
                device_session_id=request.POST.get('devsessionid')

            )

        except openpay.CardError:
            return HttpResponse('Error de tarjeta')

        if charge.status == 'completed':
            charge_reg = Charge(
                suscription=suscription,
                plan=contract_service.service,
                amount=contract_service.service.price,
                status='paid',
                card=card.card_number,

            )
            charge_reg.save()

            contract_service.adult = Adult.objects.filter(responsable=client)[0]

            client.user_type = 'User type 3'
            client.save()

        return redirect(self.success_url)


class ContractComprobation(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('landing:success_contract')
    def get(self, request):

        suscription = Suscription.objects.get(client=request.user.client)
        customer = openpay.Customer.retrieve(suscription.openpay_id)
        cards = customer.cards.all()

        contract_service = HiredService.objects.get(client=request.user.client)
        service_days = ServiceDay.objects.filter(service=contract_service)
        activities = []
        workshops = []
        for x in service_days:
            if x.content_object.__class__ is Activity:
                activities.append(x.content_object)
            if x.content_object.__class__ is Workshop:
                workshops.append(x.content_object)
        ctx = {
            'contract_service': contract_service,
            'activities': activities,
            'workshops': workshops,
            'card': cards.data[0]
        }


        return TemplateResponse(request, 'services/contract_comprobation.html', ctx)


class ContractUnique(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('landing:success_contract')

    def get(self, request):
        return TemplateResponse(request, 'services/contract_unique.html')
    def post(self, request):
        description = request.POST.get('description')
        day = request.POST.get('day')
        month = request.POST.get('month')
        street = request.POST.get('street')
        num_ext = request.POST.get('num_ext')
        num_int = request.POST.get('num_int')
        colony = request.POST.get('colony')
        delegation = request.POST.get('delegation')
        cp = request.POST.get('cp')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        service = UniqueService(
            client=request.user.client,
            description=description,
            day=day,
            month=month,
            street=street,
            num_ext=num_ext,
            num_int=num_int,
            colony=colony,
            delegation=delegation,
            cp=cp,
            time=time,
            duration=duration
        )

        service.save()

        return redirect(self.success_url)