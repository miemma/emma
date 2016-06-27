#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from emma.apps.adults.models import Adult, AdultAddress
from emma.apps.services.models import HiredService, Service, Workshop, \
    ServiceDays
from emma.apps.clients.models import ContractProcess
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
                'placeholder': 'Dia'
            }
        ),
        required=True,
        validators=[validators.eval_blank]
    )
    day_1_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_2_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_3_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_4_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_5_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_6_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Dia'
            }
        ),
        required=False
    )
    day_7_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input contract-location-form-input',
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
                'placeholder': 'Hora'
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
                'placeholder': 'Hora',
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
        contract_process = ContractProcess.objects.get(
            client=self.request.user.client
        )
        try:
            service_address = AdultAddress.objects.get(
                id=contract_process.adult_address_id
            )
            service_address.street = cleaned_data.get('street')
            service_address.outdoor_number = cleaned_data.get('num_ext')
            service_address.colony = cleaned_data.get('colony')
            service_address.municipality = cleaned_data.get('delegation')
            service_address.postal_code = cleaned_data.get('cp')
            service_address.city = 'Ciudad de México'
            service_address.state = 'México'
            service_address.reference = cleaned_data.get('address_reference')
        except AdultAddress.DoesNotExist:
            service_address = AdultAddress(
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

        contract_process.adult_address_id = service_address.id
        contract_process.save()

        service = Service.objects.get(
            id=contract_process.id_service
        )

        workshop_list = []
        for x in contract_process.workshop_list:
            if x.isdigit():
                workshop_list.append(x)

        workshops = ''
        num_workshops = 0
        for workshop in workshop_list:
            work = Workshop.objects.get(id=workshop, service=service)
            workshops += '%s, ' % str(work.name)
            num_workshops += 1
        workshops = workshops[:-2]


        start_date = self.cleaned_data.get('start_date')

        try:
            hired_service = HiredService.objects.get(
                client=self.request.user.client
            )
            hired_service.service = Service.objects.get(
                id=contract_process.id_service
            )
            hired_service.workshops = workshops
            hired_service.num_workshops = num_workshops
            hired_service.start_date = start_date
        except HiredService.DoesNotExist:
            hired_service = HiredService(
                client=self.request.user.client,
                service=Service.objects.get(
                    id=contract_process.id_service
                ),
                workshops=workshops,
                num_workshops=num_workshops,
                start_date=start_date,

            )

        day_1 = '%s %s %s' % (
            self.cleaned_data.get('day_1'),
            self.cleaned_data.get('day_1_hour'),
            self.cleaned_data.get('day_1_morning'),
        )

        service_days = ServiceDays(
            name="Service Days - %s" % self.request.user.email,
            service_day_1=day_1
        )

        if self.cleaned_data.get('day_2'):
            day_2 = '%s %s %s' % (
                self.cleaned_data.get('day_2'),
                self.cleaned_data.get('day_2_hour'),
                self.cleaned_data.get('day_2_morning'),
            )

            service_days.service_day_2 = day_2

        if self.cleaned_data.get('day_3'):
            day_3 = '%s %s %s' % (
                self.cleaned_data.get('day_3'),
                self.cleaned_data.get('day_3_hour'),
                self.cleaned_data.get('day_3_morning'),
            )

            service_days.service_day_3 = day_3

        if self.cleaned_data.get('day_4'):
            day_4 = '%s %s %s' % (
                self.cleaned_data.get('day_4'),
                self.cleaned_data.get('day_4_hour'),
                self.cleaned_data.get('day_4_morning'),
            )

            service_days.service_day_4 = day_4

        if self.cleaned_data.get('day_5'):
            day_5 = '%s %s %s' % (
                self.cleaned_data.get('day_5'),
                self.cleaned_data.get('day_5_hour'),
                self.cleaned_data.get('day_5_morning'),
            )

            service_days.service_day_4 = day_5

        if self.cleaned_data.get('day_6'):
            day_6 = '%s %s %s' % (
                self.cleaned_data.get('day_6'),
                self.cleaned_data.get('day_6_hour'),
                self.cleaned_data.get('day_6_morning'),
            )

            service_days.service_day_6 = day_6

        if self.cleaned_data.get('day_7'):
            day_7 = '%s %s %s' % (
                self.cleaned_data.get('day_7'),
                self.cleaned_data.get('day_7_hour'),
                self.cleaned_data.get('day_7_morning'),
            )

            service_days.service_day_7 = day_7

        service_days.save()

        hired_service.service_days = service_days

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
                'rows': '5'
            }
        ),
    )
    familiar_structure = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input contract-adult-form-area',
                'placeholder': 'Estructura Familiar',
                'rows': '5'
            }
        ),
    )
    personality = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input contract-adult-form-area',
                'placeholder': 'Personalidad',
                'rows': '5'
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
            if field == 'birthday':
                self.fields[field].validators = [validators.eval_blank,
                                                 validators.eval_date]

    def save(self):
        cleaned_data = super(ContractAdultInfo, self).clean()

        try:
            adult = Adult.objects.get(responsable=self.request.user.client)
            adult.first_name = cleaned_data.get('name')
            adult.last_name = cleaned_data.get('last_name')
            adult.birthday = cleaned_data.get('birthday')
            adult.description = cleaned_data.get('description')
            adult.personality = cleaned_data.get('personality')
            adult.familiar_structure = cleaned_data.get('familiar_structure')
        except Adult.DoesNotExist:
            adult = Adult(
                first_name=cleaned_data.get('name'),
                last_name=cleaned_data.get('last_name'),
                birthday=cleaned_data.get('birthday'),
                responsable=self.request.user.client,
                personality=cleaned_data.get('personality'),
                familiar_structure=cleaned_data.get('familiar_structure'),
                description=cleaned_data.get('description')
            )

        adult.save()

        service = HiredService.objects.get(
            client=self.request.user.client
        )

        service.adult = adult

        service.save()