#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.models import Adult
from emma.apps.clients.forms import UserInformationForm
from emma.apps.clients.models import Client
from emma.apps.suscriptions.models import Suscription
from emma.apps.xauth.forms import UpdatePasswordForm
from emma.core.mixins import ClientRequiredMixin, LoginRequiredMixin, \
    GetAdultMixin

import openpay


class ClientDetailView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'clients/client_detail.html'

    def get(self, request, **kwargs):
        password_form = UpdatePasswordForm()
        ctx = {
            'password_form':password_form,
            'user_form':self.get_user_initial_form(request),
            'adult':self.get_adult(request)
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        kwargs = {'request':request}
        if 'user_information' in request.POST:
            user_form = UserInformationForm(request.POST, **kwargs)
            if user_form.is_valid():
                user_form.save()
                ctx = {
                    'password_form': UpdatePasswordForm(),
                    'user_form': self.get_user_initial_form(request),
                    'success': 'El usuario ha sido actualizado'
                }
            else:
                ctx = {
                    'password_form': UpdatePasswordForm(),
                    'user_form': user_form,
                }
            return TemplateResponse(request, self.template_name, ctx)
        elif 'user_password' in request.POST:
            password_form = UpdatePasswordForm(request.POST, **kwargs)
            if password_form.is_valid():
                password_form.save()
                ctx = {
                    'password_form': UpdatePasswordForm(),
                    'user_form': self.get_user_initial_form(request),
                    'success': 'La contraseña ha sido actualizada'
                }
            else:
                ctx = {
                    'password_form': password_form,
                    'user_form': self.get_user_initial_form(request),
                }
            return TemplateResponse(request, self.template_name, ctx)
        else:
            raise Http404("No se encontro la pagina")

    def get_user_initial_form(self, request):
        form = UserInformationForm(
            initial=  {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'contact_number': request.user.client.contact_number,
            }
        )
        return form


class AddCardView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'clients/add_card.html'

    def get(self, request, **kwargs):
        ctx = {
            'adult': self.get_adult(request)
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        client = Client.objects.get(user=request.user)
        suscription = Suscription.objects.get(client=client)
        customer = openpay.Customer.retrieve(suscription.openpay_id)

        card = customer.cards.create(
            token_id=request.POST['token_id'],
            device_session_id=request.POST['devsessionid']
        )
        return redirect(reverse_lazy('clients:dashboard_add_card'))


class WelcomeView(ClientRequiredMixin, View):
    def get(self, request, **kwargs):
        client = request.user.client
        if client.user_type == 'User type 1':
            ctx = {'make_call': 'true'}
            return TemplateResponse(request, 'clients/welcome.html', ctx)
        elif client.user_type == 'User type 2':
            ctx = {'contract_service': 'true'}
            return TemplateResponse(request, 'clients/welcome.html', ctx)
        elif client.user_type == 'User type 3' and hasattr(client, 'suscriptions'):
            if client.first_time_dashboard:
                client.first_time_dashboard = True
                client.save()
                ctx = {'view_profile': 'true'}
                return TemplateResponse(request, 'clients/welcome.html', ctx)
            else:
                return redirect(reverse('adults:dashboard_adult'))
