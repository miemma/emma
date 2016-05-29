#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from emma.apps.adults.models import Adult, Doctor
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
        required=True,
        validators=[validators.eval_blank]
    )
    num_ext = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Num. Ext'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    num_int = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Num. Int'
            }
        ),
        required=False,
        validators=[validators.eval_blank]
    )
    colony = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Colonia'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    delegation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Delegación'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    cp = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'C.P'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    address_reference = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input contract-location-form-area',
                'placeholder': 'Referencia',
                'rows': '4'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    day_1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Lunes)'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    day_1_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=True,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_1_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=True
    )
    day_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Martes)'
            }
        ),
        required=False
    )
    day_2_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_2_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    day_3 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Miércoles)'
            }
        ),
        required=False
    )
    day_3_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_3_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    day_4 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Jueves)'
            }
        ),
        required=False
    )
    day_4_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_4_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    day_5 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Viernes)'
            }
        ),
        required=False
    )
    day_5_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_5_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    day_6 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Sábado)'
            }
        ),
        required=False
    )
    day_6_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_6_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    day_7 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Dia (Ej: Domingo)'
            }
        ),
        required=False
    )
    day_7_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=False,
        validators=[validators.eval_blank,
                    validators.eval_time]
    )
    day_7_morning = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input '
                         'contract-location-form-input-morning',
                'placeholder': 'Hora (Ej: 12:00)',
                'value': 'AM',
                'readonly': 'true'
            }
        ),
        required=False
    )
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Fecha (DD/MM/AAAA)'
            }
        ),
        required=True,
        validators=[validators.eval_date]
    )

    start_time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora (Ej: 12:00)'
            }
        ),
        required=True,
        validators=[validators.eval_blank,
                    validators.eval_time]
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
        required=True
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServiceData, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages = error_messages
    def save(self):
        cleaned_data = super(ServiceData, self).clean()
        try:
            service_address = Address.objects.get(user=self.request.user)
            service_address.street = cleaned_data.get('street')
            service_address.outdoor_number = cleaned_data.get('num_ext')
            service_address.colony = cleaned_data.get('colony')
            service_address.municipality = cleaned_data.get('delegation')
            service_address.postal_code = cleaned_data.get('cp')
            service_address.city = 'Ciudad de México'
            service_address.state = 'México'
            service_address.reference = cleaned_data.get('address_reference')
        except Address.DoesNotExist:
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

        service_address.save()

        service = Service.objects.get(
            id=self.request.session['id_service']
        )

        workshop_list = self.request.session['workshop_list']
        workshops = ''
        num_workshops = 0
        for workshop in workshop_list:
            work = Workshop.objects.get(id=workshop, service=service)
            workshops += '%s, ' % str(work.name)
            num_workshops += 1
        workshops = workshops[:-2]

        day_1 = '%s %s %s' % (
            self.cleaned_data.get('day_1'),
            self.cleaned_data.get('day_1_hour'),
            self.cleaned_data.get('day_1_morning'),
        )


        start_date = self.cleaned_data.get('start_date')

        try:
            hired_service = HiredService.objects.get(
                client=self.request.user.client
            )
            hired_service.service = Service.objects.get(
                id=self.request.session['id_service']
            )
            hired_service.workshops = workshops
            hired_service.num_workshops = num_workshops
            hired_service.start_date = start_date
            hired_service.service_day_1 = day_1
        except HiredService.DoesNotExist:
            hired_service = HiredService(
                client=self.request.user.client,
                service=Service.objects.get(
                    id=self.request.session['id_service']
                ),
                workshops=workshops,
                num_workshops=num_workshops,
                start_date=start_date,
                service_day_1 = day_1,

            )

        if self.cleaned_data.get('day_2'):
            day_2 = '%s %s %s' % (
                self.cleaned_data.get('day_2'),
                self.cleaned_data.get('day_2_hour'),
                self.cleaned_data.get('day_2_morning'),
            )

            hired_service.service_day_2 = day_2

        if self.cleaned_data.get('day_3'):
            day_3 = '%s %s %s' % (
                self.cleaned_data.get('day_3'),
                self.cleaned_data.get('day_3_hour'),
                self.cleaned_data.get('day_3_morning'),
            )

            hired_service.service_day_3 = day_3

        if self.cleaned_data.get('day_4'):
            day_4 = '%s %s %s' % (
                self.cleaned_data.get('day_4'),
                self.cleaned_data.get('day_4_hour'),
                self.cleaned_data.get('day_4_morning'),
            )

            hired_service.service_day_4 = day_4

        if self.cleaned_data.get('day_5'):
            day_5 = '%s %s %s' % (
                self.cleaned_data.get('day_5'),
                self.cleaned_data.get('day_5_hour'),
                self.cleaned_data.get('day_5_morning'),
            )

            hired_service.service_day_4 = day_5

        if self.cleaned_data.get('day_6'):
            day_6 = '%s %s %s' % (
                self.cleaned_data.get('day_6'),
                self.cleaned_data.get('day_6_hour'),
                self.cleaned_data.get('day_6_morning'),
            )

            hired_service.service_day_6 = day_6

        if self.cleaned_data.get('day_7'):
            day_7 = '%s %s %s' % (
                self.cleaned_data.get('day_7'),
                self.cleaned_data.get('day_7_hour'),
                self.cleaned_data.get('day_7_morning'),
            )

            hired_service.service_day_7 = day_7

        hired_service.save()

class ContractAdultInfo(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'Nombre'
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'Apellidos'
            }
        ),
    )
    birthday = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'DD/MM/AAAA'
            }
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input contract-adult-form-area',
                'placeholder': 'Descripción',
                'rows': '8'
            }
        ),
    )
    doctor_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'Nombre del médico'
            }
        ),
    )
    doctor_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'Teléfono del médico'
            }
        ),
    )
    doctor_cp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-adult-form-input',
                'placeholder': 'C.P'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ContractAdultInfo, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages
            self.fields[field].validators = [validators.eval_blank]

    def save(self):
        cleaned_data = super(ContractAdultInfo, self).clean()

        adult = Adult(
            first_name=cleaned_data.get('name'),
            last_name=cleaned_data.get('last_name'),
            birthday=cleaned_data.get('birthday'),
            responsable=self.request.user.client,
        )

        doctor = Doctor(
            name=cleaned_data.get('doctor_name'),
            phone=cleaned_data.get('doctor_phone'),
            cp=cleaned_data.get('doctor_cp')
        )

        adult.save()

        doctor.save()

        service = HiredService.objects.filter(
            client=self.request.user.client
        )[0]

        service.adult = adult

        service.save()