#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import print_function

import json
import urlparse
from datetime import date

import requests
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.views.generic import View, TemplateView, ListView
from django.conf import settings

from emma.apps.clients.models import PotentialClient
from emma.apps.emmas.models import PotentialEmma
from emma.apps.newsletter.models import BlogSubscriber
from emma.apps.services.models import Service, ScheduledCall
from emma.core.mixins import ClientRequiredMixin
from emma.core.utils import send_email


class HomeTemplateView(View):
    @staticmethod
    def get(request):
        today = date.today()
        context = {
            'today': today.strftime("%m/%d/%Y")
        }
        return render(request, 'landing/index.html', context)


class ServicesTemplateView(ListView):
    @staticmethod
    def get_context(request):
        plans = Service.objects.all()
        ctx = {
            'plans': plans
        }
        return ctx

    def get(self, request):
        ctx = self.get_context(request)
        return TemplateResponse(request, 'landing/services.html', ctx)


class FAQTemplateView(TemplateView):
    template_name = 'landing/how.html'


class AboutTemplateView(TemplateView):
    template_name = 'landing/about.html'


class WhoTemplateView(TemplateView):
    template_name = 'landing/who.html'


class SuccessTemplateView(TemplateView):
    template_name = 'landing/success.html'


class SuccessPayTemplateView(TemplateView):
    template_name = 'landing/success_pay.html'


class SuccessContractTemplateView(TemplateView):
    template_name = 'landing/success_contract.html'


class ContactEmailView(View):
    @staticmethod
    def post(request):
        email = request.POST.get('email')
        sender = request.POST.get('sender')
        message = request.POST.get('message')

        ctx = {
            'sender': sender,
            'email': email,
            'message': message
        }

        send_email(
            subject='email/subjects/contact.txt',
            body='email/contact.html',
            from_email="Emma - Contacto <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[settings.DEFAULT_EMAIL_TO],
            context=ctx
        )

        customer = PotentialClient(
            name=sender,
            email=email,
            source='Contacto'
        )
        customer.save()

        return redirect(reverse('landing:success'))


class JoinEmailView(View):
    @staticmethod
    def get(request):
        return render(request, 'landing/join.html')

    @staticmethod
    def post(request):
        last_name = request.POST.get('last_name')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone_movile = request.POST.get('phone_movile')
        phone = request.POST.get('phone')
        education = request.POST.get('join-education-value')
        city = request.POST.get('city')
        state = request.POST.get('state')
        litte_city = request.POST.get('litte_city')
        colony = request.POST.get('colony')
        postal_code = request.POST.get('postal_code')
        know = request.POST.getlist('join-source-value')
        xknow = ''
        for x in know:
            xknow += '%s, ' % str(x)
        xknow = xknow[:-1]
        facebook = request.POST.get('join-facebook-value')
        if facebook == 'si':
            bool_facebook = True
        else:
            bool_facebook = False
        smartphone = request.POST.get('join-smartphone-value')
        if smartphone == 'si':
            bool_smartphone = True
        else:
            bool_smartphone = False

        ctx = {
            'name': name,
            'last_name': last_name,
            'email': email,
            'age': age,
            'phone_movile': phone_movile,
            'phone': phone,
            'education': education,
            'city': city,
            'state': state,
            'litte_city': litte_city,
            'colony': colony,
            'postal_code': postal_code,
            'xknow': xknow,
            'facebook': facebook,
            'smartphone': smartphone,
        }

        potential_emma = PotentialEmma(
            first_name=name,
            last_name=last_name,
            age=age,
            movile_phone=phone_movile,
            phone=phone_movile,
            school_grade=education,
            address='%s %s %s %s %s' % (
                city, state, litte_city, colony, postal_code
            ),
            how_met_emma=xknow,
            has_facebook=bool_facebook,
            has_smathphone=bool_smartphone
        )
        potential_emma.save()

        send_email(
            subject='email/subjects/join_emma.txt',
            body='email/join_emma.html',
            from_email="Emma - Reclutamiento <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[settings.DEFAULT_EMAIL_TO,
                      settings.DEFAULT_JOIN_EMAIL_TO],
            context=ctx
        )

        return redirect(reverse('landing:success'))


class DateEmailView(ClientRequiredMixin, View):
    @staticmethod
    def get(request):
        today = date.today()
        context = {
            'today': today.strftime("%m/%d/%Y")
        }
        return render(request, 'landing/date.html', context)

    @staticmethod
    def post(request):
        email = request.user.email
        name = request.user.first_name
        last_name = request.user.get_full_last_name

        number = request.POST.get('number')
        minute = request.POST.get('minute')
        hour = request.POST.get('hour')
        tempo = request.POST.get('morning')
        time = '%s:%s' % (hour, minute)
        datet = request.POST.get('date_input')
        tz = request.POST.get('timezone')

        ctx = {
            'name': name,
            'last_name': last_name,
            'email': email,
            'number': number,
            'tempo': tempo,
            'time': time,
            'date': datet,
            'tz': tz,

        }

        send_email(
            subject='email/subjects/call_schedule.txt',
            body='email/call_schedule.html',
            from_email="Emma - Ventas <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[settings.DEFAULT_EMAIL_TO],
            context=ctx
        )

        send_email(
            subject='email/subjects/notification_call.txt',
            body='email/notification_call.html',
            from_email="Emma - Notificaciones <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[email],
            context=ctx
        )

        call = ScheduledCall(
            name="%s %s" % (name, last_name),
            email=email,
            date_time="%s %s:%s" % (datet, hour, minute),
            number=number

        )
        call.save()

        customer = PotentialClient(
            name="%s %s" % (name, last_name),
            email=email,
            source='Agendar una Cita'
        )
        customer.save()

        return redirect(reverse('landing:success'))


class NewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(NewsletterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('This is a get')

    def post(self, request):
        source = request.POST.get('source')
        email = request.POST.get('email')
        endpoint = urlparse.urljoin(
            settings.MAILCHIMP_API_ROOT,
            'lists/%s/members/' % settings.MAILCHIMP_NEWSLETTER_LIST
        )
        data = {
            "email_address": request.POST.get('email'),
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', settings.MAILCHIMP_API_KEY), data=data)
        if email:
            try:
                subscriber = BlogSubscriber.objects.get(
                    email=email,
                    source=source,
                )
            except BlogSubscriber.DoesNotExist:
                subscriber = BlogSubscriber(
                    email=email,
                    source=source,
                )
                subscriber.save()
        return JsonResponse(response.json())


class AlternativeJoinEmmaView(TemplateView):
    template_name = 'landing/alternative_join.html'


class PrivacyTemplateView(TemplateView):
    template_name = 'landing/privacy.html'
