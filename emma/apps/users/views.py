#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView, View

import openpay

from emma.apps.suscriptions.models import Suscription, History, Charge
from emma.apps.users.models import Client
from emma.core.mixins import RequestFormMixin, AuthRedirectMixin, \
    LoginRequiredMixin, NextUrlMixin, ClientRequiredMixin

from emma.apps.users.forms import ChangePasswordForm, LoginForm


class SelectCardView(ClientRequiredMixin, View):
    template_name = 'users/select_card.html'

    def get(self, request):
        client = Client.objects.get(user=request.user)
        suscription = Suscription.objects.get(user=client)
        customer = openpay.Customer.retrieve(suscription.id_customer)
        cards = customer.cards.all()

        ctx = {
            'cards': cards.data
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        suscription = Suscription.objects.get(user=request.user.client)
        customer = openpay.Customer.retrieve(suscription.id_customer)
        card = customer.cards.retrieve(request.POST['customer-card'])
        openpay_charge = openpay.Charge.create(
            source_id=card.id,
            method="card",
            amount=request.POST['service_ammount'],
            currency="MXN",
            description="Charge for Emma service",
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
        return  redirect(reverse_lazy('landing:success_pay'))


class AddCardView(ClientRequiredMixin, View):
    template_name = 'users/add_card.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        client = Client.objects.get(user=request.user)
        try:
            suscription = Suscription.objects.get(user=client)
            customer = openpay.Customer.retrieve(suscription.id_customer)
            card = customer.cards.create(
                token_id=request.POST['token_id'],
                device_session_id=request.POST['devsessionid']
            )
            openpay_charge = openpay.Charge.create(
                source_id=card.id,
                method="card",
                amount=100,
                currency="MXN",
                description="Charge for Emma service",
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
        except Suscription.DoesNotExist:
            customer = openpay.Customer.create(
                name=request.user.get_full_name(),
                email=request.user.email,
                requires_account=False,
                status='active',
            )
            card = customer.cards.create(
                token_id=request.POST['token_id'],
                device_session_id=request.POST['devsessionid']
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
                movement="Suscription Created"
            )
            history.save()
            openpay_charge = openpay.Charge.create(
                source_id=card.id,
                method="card",
                amount=3600,
                currency="MXN",
                description="Charge for paid Emma service",
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
            return redirect(reverse_lazy('landing:success_pay'))


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)


class LoginView(NextUrlMixin, AuthRedirectMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


@login_required(login_url=reverse_lazy('users:login'))
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('landing:home'))
