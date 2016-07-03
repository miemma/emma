#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import get_object_or_404

from emma.apps.adults.models import Adult, AdultAddress, \
    MedicalInfo as medical_info
from emma.core import validators
from emma.core.messages import error_messages


class AdultInfo(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Nombre'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Apellido'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class': '',
            }
        ),
        required = True,

    )
    street = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Calle'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    num_ext = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Num. Ext'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    num_int = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Num. Int'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    delegation = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': '',
                'placeholder': 'Delegacion'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages,
        choices=(
            ('Álvaro Obregón', 'Álvaro Obregón',),
            ('Azcapotzalco', 'Azcapotzalco',),
            ('Benito Juárez', 'Benito Juárez',),
            ('Coyoacán', 'Coyoacán',),
            ('Cuajimalpa de Morelos', 'Cuajimalpa de Morelos',),
            ('Cuauhtémoc', 'Cuauhtémoc',),
            ('Coyoacán', 'Coyoacán',),
            ('Gustavo A. Madero', 'Gustavo A. Madero',),
            ('Iztacalco', 'Iztacalco',),
            ('Iztapalapa', 'Iztapalapa',),
            ('Magdalena Contreras', 'Magdalena Contreras',),
            ('Miguel Hidalgo', 'Miguel Hidalgo',),
            ('Milpa Alta', 'Milpa Alta',),
            ('Tláhuac', 'Tláhuac',),
            ('Tlalpan', 'Tlalpan',),
            ('Venustiano Carranza', 'Venustiano Carranza',),
            ('Xochimilco', 'Xochimilco',),
        )
    )
    colony = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Delegacion'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Codigo Postal'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    reference = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': 'Referencia'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    photo = forms.ImageField(
        required=False,
        error_messages=error_messages
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.adult_id = kwargs.pop('adult_id', None)
        super(AdultInfo, self).__init__(*args, **kwargs)


    def save(self):
        cleaned_data = super(AdultInfo, self).clean()

        client = self.request.user.client

        if not self.adult_id:
            adult = Adult.objects.filter(responsable=client)[0]
        else:
            adult = get_object_or_404(Adult,
                                      responsable=client, id=int(self.adult_id))

        address = AdultAddress.objects.get(adult=adult)

        adult.first_name = cleaned_data.get('first_name')
        adult.last_name = cleaned_data.get('last_name')
        adult.birthday = cleaned_data.get('birthday')

        if cleaned_data.get('photo'):
            adult.photo = cleaned_data.get('photo')

        adult.save()

        address.street = cleaned_data.get('street')
        address.outdoor_number = cleaned_data.get('num_ext')
        address.interior_number = cleaned_data.get('num_int')
        address.municipality = cleaned_data.get('delegation')
        address.colony = cleaned_data.get('colony')
        address.postal_code = cleaned_data.get('postal_code')
        address.reference = cleaned_data.get('reference')

        address.save()


class MedicalInfo(forms.Form):
    blood_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': '',
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages,
        choices=(
            ('AB+', 'AB+',),
            ('AB-', 'AB-',),
            ('A+', 'A+',),
            ('A-', 'A-',),
            ('B+', 'B+',),
            ('B-', 'B-',),
            ('O+', 'O+',),
            ('O-', 'O-',),
        )
    )
    emergency_contact_1_full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Nombre Completo'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_1_relation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Relacion con la persona mayor'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_1_cell_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono móvil'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_1_home_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono de casa'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_2_full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Nombre Completo'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_2_relation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Relacion con la persona mayor'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_2_cell_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono móvil'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    emergency_contact_2_home_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono de casa'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    knows_pda = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': '',
            }
        ),
    )
    exercise_pda = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': '',
            }
        ),
    )
    has_medical_insurance = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': '',
            }
        ),
    )
    insurance_company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Compañia de seguros'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    policy_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Numero de poliza'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    policy_expiration_date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class': '',
            }
        ),
        required=True,
    )
    has_social_security = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': '',
            }
        ),
    )
    social_security_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Numero de seguridad social'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )

    doctor_first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Nombre'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )

    doctor_last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Apellido'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    doctor_cell_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono móvil'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    doctor_home_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono de casa'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    doctor_working_institution = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Institución donde trabaja'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    doctor_professional_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Teléfono de casa'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    diseases = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': '¿Qué enfermedades o padecimientos presenta?'
            }
        ),
        required=True,
        error_messages=error_messages
    )
    current_medications = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': 'Medicacion Actual'
            }
        ),
        required=True,
        error_messages=error_messages
    )
    drug_allergy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': 'Alergias a medicamentos'
            }
        ),
        required=True,
        error_messages=error_messages
    )
    food_allergy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': 'Alergias a alimentos'
            }
        ),
        required=True,
        error_messages=error_messages
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.adult_id = kwargs.pop('adult_id', None)
        super(MedicalInfo, self).__init__(*args, **kwargs)


    def save(self):
        cleaned_data = super(MedicalInfo, self).clean()

        client = self.request.user.client

        if not self.adult_id:
            adult = Adult.objects.filter(responsable=client)[0]
        else:
            adult = get_object_or_404(Adult,
                                      responsable=client,
                                      id=int(self.adult_id))
        medical_information = medical_info.objects.get(adult=adult)

        medical_information.blood_type = cleaned_data.get('blood_type')

        medical_information.save()

        contact_1 = adult.medical_information.emergency_contact_1

        contact_1.save()
