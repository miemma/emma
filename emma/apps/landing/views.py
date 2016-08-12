#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import print_function
from datetime import date

from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
from django.conf import settings

from emma.apps.clients.models import PotentialClient
from emma.apps.emmas.models import PotentialEmma
from emma.apps.services.models import ScheduledCall
from emma.core.mixins import ClientRequiredMixin
from emma.core.utils import send_email


class HomeTemplateView(TemplateView):
    template_name = 'landing/index.html'


class ServicesTemplateView(TemplateView):
    template_name = 'landing/services.html'


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
        smartphone = request.POST.get('join-smartphone-value')

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

        potential_emma =  PotentialEmma(
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
            has_facebook=facebook,
            has_smathphone=smartphone
        )
        potential_emma.save()

        send_email(
            subject='email/subjects/join_emma.txt',
            body='email/join_emma.html',
            from_email="Emma - Reclutamiento <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[settings.DEFAULT_JOIN_EMAIL_TO],
            context=ctx
        )

        customer = PotentialClient(
            name='%s %s' % (name, last_name),
            email=email,
            source='Unete a emma'
        )
        customer.save()

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
