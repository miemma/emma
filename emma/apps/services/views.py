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
from emma.apps.services.models import Service, Workshop, HiredService, \
    ServiceContractProcess, ServiceDay, Activity
from emma.apps.suscriptions.models import Suscription, History
from emma.core.mixins import RequestFormMixin, ActiveClientRequiredMixin

from datetime import datetime, date


class ContractPlan(ActiveClientRequiredMixin, View):
    success_url = reverse_lazy('services:contract_location')

    def get_context(self, request):
        plans = Service.objects.all()
        ctx = {
            'plans': plans
        }
        return ctx

    def get(self, request, **kwargs):
        ctx = self.get_context(request)
        return TemplateResponse(request, 'services/contract_plan.html', ctx)

    def post(self, request):
        plan = Service.objects.get(id=request.POST.get('plan'))
        service = ServiceContractProcess(
            user=request.user.client,
            plan=plan
        )
        service.save()
        return HttpResponse(plan)


class ContractPlanDetails(ActiveClientRequiredMixin, View):
    def get_context(self, request):
        workshops = Workshop.objects.all()
        activities = Activity.objects.all()
        service = ServiceContractProcess.objects.get(
            user=request.user.client,
        )
        weekly_sessions = range(1, service.plan.max_weekly_sessions + 1)
        weekly_hours = range(1, service.plan.weekly_hours + 1)
        ctx = {
            'workshops': workshops,
            'activities': activities,
            'service': service,
            'weekly_sessions': weekly_sessions,
            'weekly_hours': weekly_hours
        }
        return ctx

    def get(self, request, **kwargs):
        ctx = self.get_context(request)
        return TemplateResponse(request, 'services/contract_details.html', ctx)

    def post(self, request, **kwargs):
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        contract_process = ServiceContractProcess.objects.get(user=request.user.client)
        for x in days:
            if request.POST.get('%s_day' % x):
                workshop_activity = request.POST.get('%s_workshop_activity' % x).split('-')
                try:
                    content = Workshop.objects.get(id=workshop_activity[0], name=workshop_activity[1])
                except Workshop.DoesNotExist:
                    try:
                        content = Activity.objects.get(id=workshop_activity[0], name=workshop_activity[1])
                    except Activity.DoesNotExist:
                        raise Http404
                service_day = ServiceDay(
                    day=request.POST.get('%s_day' % x),
                    start_time=request.POST.get('%s_start_time' % x),
                    duration=request.POST.get('%s_weekly_sessions' % x),
                    content_object=content
                )
                service_day.save()
                contract_process.service_days.add(service_day)
                contract_process.save()
        return HttpResponse('Hola')


class ContractEmmaPreference(ActiveClientRequiredMixin, View):
    def get(self, request, **kwargs):
        return TemplateResponse(request, 'services/contract_emma.html')
    def post(self, request, **kwargs):
        contract_process = ServiceContractProcess.objects.get(user=request.user.client)
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
        return HttpResponse('Hola')


class ContractPay(ActiveClientRequiredMixin, View):
    def get(self, request):
        return render(request, 'services/contract_pay.html')

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


        return redirect(reverse_lazy('landing:success_contract'))


class ContractComprobation(ActiveClientRequiredMixin, View):
    def get(self, request):
        contract_service = ServiceContractProcess.objects.get(user=request.user.client)
        ctx = {
            'contract_service': contract_service
        }
        return TemplateResponse(request, 'services/contract_comprobation.html', ctx)