#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import print_function
from datetime import date, timedelta

from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
from django.conf import settings

from .models import Customer


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


class ContactEmailView(View):
    def post(self, request):
        email = request.POST.get('email')
        sender = request.POST.get('sender')
        message = request.POST.get('message')

        msg = EmailMultiAlternatives(
            subject="Un cliente requiere mayor información",
            from_email="Emma - Contacto <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to=[settings.DEFAULT_EMAIL_TO]
        )
        msg.attach_alternative(
            "<p>Nombre del cliente: %s </p>"
            "<p>Correo electronico: %s </p>"
            "<p>Mensaje: %s </p>" % (sender, email, message),
            "text/html"
        )
        msg.send()

        customer = Customer (
            name=sender,
            email=email,
            source='Contacto'
        )
        customer.save()

        return redirect(reverse('landing:success'))


class JoinEmailView(View):
    def get(self, request):
        return render(request, 'landing/join.html')

    def post(self, request):
        last_name = request.POST.get('last_name')
        name = request.POST.get('name')
        age =request.POST.get('age')
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
        facebook = request.POST.get('join-facebook-value')
        smartphone = request.POST.get('join-smartphone-value')

        msg = EmailMultiAlternatives(
            subject="Solicitud para ser Emma",
            from_email="Emma - Reclutamiento <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to=[settings.DEFAULT_EMAIL_TO, 'fernanda@miemma.com']
        )
        msg.attach_alternative(
            "<p>Nombre: %s %s </p>"
            "<p>Edad: %s </p>"
            "<p>Correo electronico: %s </p>"
            "<p>Telefono movil: %s </p>"
            "<p>Telefono fijo: %s </p>"
            "<p>Escolaridad: %s </p>"
            "<p>Ciudad: %s </p>"
            "<p>Estado: %s </p>"
            "<p>Delegacion/Municipio: %s </p>"
            "<p>Colonia: %s </p>"
            "<p>Codigo Postal: %s </p>"
            "<p>Como conocio a emma: %s </p>"
            "<p>Tiene facebook: %s </p>"
            "<p>Tiene Smartphone?: %s </p>" % (
                name, last_name, age, email, phone_movile,
                phone, education, city, state, litte_city, colony, postal_code,
                xknow, facebook, smartphone
            ), "text/html"
        )

        msg.send()

        customer = Customer(
            name=('%s %s') % (name, last_name),
            email=email,
            source='Unete a emma'
        )
        customer.save()

        return redirect(reverse('landing:success'))


class DateEmailView(View):
    def get(self, request):
        today = date.today()
        context = {
            'today': today.strftime("%m/%d/%Y")
        }
        return render(request, 'landing/date.html', context)

    def post(self, request):
        name = request.POST.get('name')
        email =request.POST.get('email')
        number = request.POST.get('number')
        minute = request.POST.get('minute')
        hour = request.POST.get('hour')
        tempo = request.POST.get('morning')
        time = '%s:%s' % (hour, minute)
        date = request.POST.get('date_input')

        msg = EmailMultiAlternatives(
            subject="Tienes una llamada agendada",
            from_email="Emma - Ventas <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to=[settings.DEFAULT_EMAIL_TO]
        )
        msg.attach_alternative(
            "<p>Nombre: %s </p>"
            "<p>Correo electronico: %s </p>"
            "<p>Telefono : %s </p>"
            "<p>Hora: %s %s</p>"
            "<p>Fecha: %s </p>" % (
                name, email, number, time, tempo, date
            ), "text/html"
        )

        msg.send()

        customer = Customer(
            name=name,
            email=email,
            source='Agendar una Cita'
        )
        customer.save()

        return redirect(reverse('landing:success'))
