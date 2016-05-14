#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import FormView, View

import openpay

from emma.core.utils import send_email
from emma.apps.suscriptions.models import Suscription, History, Charge
from emma.apps.clients.models import Client
from emma.core.mixins import RequestFormMixin, \
    LoginRequiredMixin, ClientRequiredMixin
from emma.apps.users.forms import ChangePasswordForm


class SelectCardView(ClientRequiredMixin, View):
    template_name = 'users/select_card.html'

    def get(self, request):
        client = Client.objects.get(user=request.user)
        if client.active_client:
            try:
                suscription = Suscription.objects.get(user=client)
            except Suscription.DoesNotExist:
                suscription = None

            if suscription is not None:
                customer = openpay.Customer.retrieve(suscription.id_customer)
                cards = customer.cards.all()

                ctx = {
                    'cards': cards.data
                }
                return render(request, self.template_name, ctx)
            else:
                return redirect(reverse_lazy('users:add_card'))

        else:
            return redirect(reverse_lazy('landing:date'))

    def post(self, request):
        suscription = Suscription.objects.get(user=request.user.client)
        customer = openpay.Customer.retrieve(suscription.id_customer)
        card = customer.cards.retrieve(request.POST['customer-card'])

        openpay_charge = openpay.Charge.create(
            source_id=card.id,
            method="card",
            amount=request.POST['service_ammount'],
            currency="MXN",
            description="Cargo por servicio de emma con tarjeta actual",
            customer=customer.id,
            device_session_id=request.POST['devsessionid']
        )

        charge = Charge.objects.create(
            suscription=suscription,
            amount=openpay_charge.amount,
            status=openpay_charge.status,
            descripcion=openpay_charge.description
        )
        charge.save()

        history = History(
            suscription=suscription,
            movement="Cargo por servicio de Emma"
        )
        history.save()

        ctx = {
            'amount': request.POST['service_ammount'],
            'card': card.card_number
        }

        send_email(
            subject='email/subjects/notification_payment.txt',
            body='email/notification_payment.html',
            to_email=[request.user.email],
            context=ctx
        )

        return redirect(reverse_lazy('landing:success_pay'))


class AddCardView(ClientRequiredMixin, View):
    template_name = 'users/add_card.html'

    def get(self, request):
        client = self.request.user.client

        try:
            Suscription.objects.get(user=client)
            has_suscription = True
        except Suscription.DoesNotExist:
            has_suscription = False

        ctx = {
            'has_suscription': has_suscription
        }

        if client.active_client:
            return render(request, self.template_name, ctx)
        else:
            return redirect(reverse_lazy('landing:date'))

    def post(self, request):
        client = Client.objects.get(user=request.user)

        try:
            suscription = Suscription.objects.get(user=client)
        except Suscription.DoesNotExist:
            suscription = None

        if suscription is not None:
            customer = openpay.Customer.retrieve(suscription.id_customer)
        else:
            customer = openpay.Customer.create(
                name=request.user.get_full_name(),
                email=request.user.email,
                requires_account=False,
                status='active',
            )

            suscription = Suscription(
                user=client,
                id_customer=customer.id,
                status='active',
                active=True
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

        ctx = {
            'card': card.card_number
        }

        send_email(
            subject='email/subjects/notification_add_card.txt',
            body='email/notification_add_card.html',
            to_email=[request.user.email],
            context=ctx
        )

        openpay_charge = openpay.Charge.create(
            source_id=card.id,
            method="card",
            amount=request.POST['service_ammount'],
            currency="MXN",
            description="Cargo por servicio de emma con nueva tarjeta",
            customer=customer.id,
            device_session_id=request.POST['devsessionid']
        )

        ctx.update({'amount': request.POST['service_ammount']})

        send_email(
            subject='email/subjects/notification_payment.txt',
            body='email/notification_payment.html',
            to_email=[request.user.email],
            context=ctx
        )

        charge = Charge.objects.create(
            suscription=suscription,
            amount=openpay_charge.amount,
            status=openpay_charge.status,
            descripcion=openpay_charge.description
        )
        charge.save()

        history = History(
            suscription=suscription,
            movement="Cargo por servicio de Emma"
        )
        history.save()

        return redirect(reverse_lazy('landing:success_pay'))


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('users:select_card')

    def form_valid(self, form):
        form.save()
        client = self.request.user.client
        client.change_password = True
        client.save()
        return super(ChangePasswordView, self).form_valid(form)

