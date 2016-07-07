#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from emma.apps.clients.models import Client
from emma.apps.users.models import CoolUser
from emma.core import validators
from emma.core.messages import error_messages


class UserInformationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Nombre'
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Apellido'
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Email'
            }
        ),
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input show-as-text',
                'placeholder': 'Telefono de contacto'
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