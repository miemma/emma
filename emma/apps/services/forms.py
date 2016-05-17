#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from emma.apps.services.models import HiredService, Service, Workshop
from emma.apps.users.models import Address
from emma.core import validators
from emma.core.messages import error_messages


class ServiceData(forms.Form):
    street = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Calle'
            }
        ),
    )
    num_ext = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Num. Ext'
            }
        ),
    )
    num_int = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Num. Int'
            }
        ),
    )
    colony = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Colonia'
            }
        ),
    )
    delegation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Delegación'
            }
        ),
    )
    cp = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'C.P'
            }
        ),
    )
    address_reference = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input contract-location-form-area',
                'placeholder': 'Referencia',
                'rows': '4'
            }
        ),
    )
    hours_per_week = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Horas a la semana'
            }
        ),
    )
    services_days = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Días'
            }
        ),
    )
    frecuency = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Frecuencia'
            }
        ),
    )
    service_reference = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Referencia'
            }
        ),
    )
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Fecha (DD/MM/AAAA)'
            }
        ),
    )
    start_time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
    )
    morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServiceData, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].error_messages = error_messages
            self.fields[field].validators = [validators.eval_blank]
            if field == 'num_int':
                self.fields[field].required = False

    def save(self):
        cleaned_data = super(ServiceData, self).clean()
        service_address = Address(
            user=self.request.user,
            street=cleaned_data.get('street'),
            outdoor_number=cleaned_data.get('num_ext'),
            colony=cleaned_data.get('colony'),
            municipality=cleaned_data.get('delegation'),
            postal_code=cleaned_data.get('cp'),
            city='Ciudad de México',
            state='México',
            reference=cleaned_data.get('address_reference')
        )

        if cleaned_data.get('num_ext'):
            service_address.interior_number = cleaned_data.get('num_ext')

        hired_service = HiredService(
            client=self.request.user.client,
            service=Service.objects.get(
                id=self.request.session['id_service']
            ),
            workshop=Workshop.objects.get(
                id=self.request.session['id_service']
            ),
            hours_per_week= cleaned_data.get('hours_per_week')
        )

        service_address.save()

