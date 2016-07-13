#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django import forms
from django.shortcuts import get_object_or_404

from emma.apps.adults.models import Adult, AdultAddress, \
    MedicalInfo as medical_info
from emma.core import validators
from emma.core.messages import error_messages

this_year = datetime.date.today().year
years = range(this_year - 90, this_year)


class AdultPreferences(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Descripcion',
                'rows': 5
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    familiar_structure = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Estructura familiar',
                'rows': 5
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    personality = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Personalidad',
                'rows': 5
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.adult_id = kwargs.pop('adult_id', None)
        super(AdultPreferences, self).__init__(*args, **kwargs)

    def save(self):
        cleaned_data = super(AdultPreferences, self).clean()

        client = self.request.user.client

        if not self.adult_id:
            adult = Adult.objects.filter(responsable=client)[0]
        else:
            adult = get_object_or_404(Adult,
                                      responsable=client,
                                      id=int(self.adult_id))

        adult.personality = cleaned_data.get('personality')
        adult.description = cleaned_data.get('description')
        adult.familiar_structure = cleaned_data.get('familiar_structure')

        adult.save()


class AdultInfo(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Apellido'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=years,
            attrs={
                'class': 'emma-input',
            }
        ),
        required = True,

    )
    street = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Num. Int'
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    delegation = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Referencia',
                'rows': 5
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Nombre Completo'
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    emergency_contact_2_relation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Relacion con la persona mayor'
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    emergency_contact_2_cell_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Teléfono móvil'
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    emergency_contact_2_home_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Teléfono de casa'
            }
        ),
        validators=[validators.eval_blank],
        required=False,
        error_messages=error_messages
    )
    knows_pda = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'radio-check-button',
            }
        ),
    )
    exercise_pda = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'radio-check-button',
            }
        ),
    )
    has_medical_insurance = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'radio-check-button',
            }
        ),
    )
    insurance_company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Número de poliza'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )
    policy_expiration_date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class': 'emma-input',
            }
        ),
        required=True,
    )
    has_social_security = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'radio-check-button',
            }
        ),
    )
    social_security_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Número de seguridad social'
            }
        ),
        validators=[validators.eval_blank],
        required=True,
        error_messages=error_messages
    )

    doctor_first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
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
                'class': 'emma-input',
                'placeholder': 'Teléfono de casa'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    doctor_working_institution = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Institución donde trabaja'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    doctor_professional_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Teléfono de casa'
            }
        ),
        required=False,
        error_messages=error_messages
    )
    diseases = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': '¿Qué enfermedades o padecimientos presenta?',
                'rows': 5
            }
        ),
        required=True,
        error_messages=error_messages
    )
    current_medications = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Medicacion Actual',
                'rows': 5
            }
        ),
        required=True,
        error_messages=error_messages
    )
    drug_allergy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Alergias a medicamentos',
                'rows': 5
            }
        ),
        required=True,
        error_messages=error_messages
    )
    food_allergy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Alergias a alimentos',
                'rows': 5
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
        medical_information.knows_pda = cleaned_data.get('knows_pda')
        medical_information.exercise_pda = cleaned_data.get('exercise_pda')
        medical_information.has_medical_insurance = cleaned_data.get('has_medical_insurance')
        medical_information.insurance_company = cleaned_data.get('insurance_company')
        medical_information.insurance_company = cleaned_data.get('insurance_company')
        medical_information.policy_number = cleaned_data.get('policy_number')
        medical_information.policy_expiration_date = cleaned_data.get('policy_expiration_date')
        medical_information.has_social_security = cleaned_data.get('has_social_security')
        medical_information.social_security_number = cleaned_data.get('social_security_number')
        medical_information.diseases = cleaned_data.get('diseases')
        medical_information.current_medications = cleaned_data.get('current_medications')
        medical_information.drug_allergy = cleaned_data.get('drug_allergy')

        medical_information.save()

        contact_1 = adult.medical_information.emergency_contact_1

        contact_1.full_name = cleaned_data.get('emergency_contact_1_full_name')
        contact_1.relation =cleaned_data.get('emergency_contact_1_relation')
        contact_1.cell_phone =cleaned_data.get('emergency_contact_1_cell_phone')
        contact_1.home_phone =cleaned_data.get('emergency_contact_1_home_phone')

        contact_1.save()

        contact_2 = adult.medical_information.emergency_contact_2

        contact_2.full_name = cleaned_data.get('emergency_contact_2_full_name')
        contact_2.relation = cleaned_data.get('emergency_contact_2_relation')
        contact_2.cell_phone = cleaned_data.get('emergency_contact_2_cell_phone')
        contact_2.home_phone = cleaned_data.get('emergency_contact_2_home_phone')

        contact_2.save()

        doctor = adult.medical_information.doctor

        doctor.first_name = cleaned_data.get('doctor_first_name')
        doctor.last_name = cleaned_data.get('doctor_last_name')
        doctor.cell_phone = cleaned_data.get('doctor_cell_phone')
        doctor.home_phone = cleaned_data.get('doctor_home_phone')
        doctor.working_institution = cleaned_data.get('doctor_working_institution')
        doctor.professional_id = cleaned_data.get('professional_id')

        doctor.save()
