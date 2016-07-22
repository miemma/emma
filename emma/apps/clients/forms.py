#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpay
from django import forms

from emma.apps.clients.models import Client
from emma.apps.suscriptions.models import Suscription
from emma.apps.users.models import CoolUser
from emma.core import validators
from emma.core.messages import error_messages

from datetime import datetime


class UserInformationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Ej. Fernando'
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Ej. López Salazar'
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Ej. ejemplo@aaa.com'
            }
        ),
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Ej. 5555555555'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.request.user.email == email:
            return email
        else:
            return validators.eval_unique(email, CoolUser, 'email', 'email')

    def save(self):
        cleaned_data = super(UserInformationForm, self).clean()

        user = self.request.user

        user.first_name = cleaned_data.get('first_name')
        user.last_name = cleaned_data.get('last_name')
        user.email = cleaned_data.get('email')

        client = Client.objects.get(user=user)

        client.contact_number = cleaned_data.get('contact_number')

        user.save()
        client.save()


class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'contact_number', 'user_type',
                  'first_time_dashboard']

    def save(self, commit=True):
        client = super(ClientCreationForm, self).save(commit=False)
        client.save()

        if client.user_type == 'User type 3':

            customer = openpay.Customer.create(
                name=client.user.get_full_name(),
                email=client.user.email,
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
        return client