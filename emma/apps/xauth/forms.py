#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm as PasswdForm
from django.contrib.auth.forms import SetPasswordForm as SetPasswdForm
from django.core.validators import RegexValidator

from emma.apps.clients.models import Client
from emma.apps.users.models import CoolUser
from emma.core import validators
from emma.core.messages import error_messages


class PasswordResetRequestForm(PasswdForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-reset-req-form-input emma-input',
                'placeholder': 'Ej. ejemplo@aaa.com'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(PasswordResetRequestForm, self).__init__(*args, **kwargs)


class PasswordResetForm(SetPasswdForm):
    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-reset-form-input emma-input',
                'placeholder': 'Nueva Contraseña'
            }
        ),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-reset-form-input emma-input',
                'placeholder': 'Confirmar Contraseña'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class ChangePasswordForm(forms.Form):
    new_password_1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-form-input emma-input',
                'placeholder': 'Nueva Contraseña'
            }
        ),
    )
    new_password_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-form-input emma-input',
                'placeholder': 'Confirmar Contraseña'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password_1 = cleaned_data.get('new_password_1')
        new_password_2 = cleaned_data.get('new_password_2')
        if new_password_1 and new_password_2:
            return validators.eval_matching(new_password_1, new_password_2)

    def save(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        user_instance = self.request.user
        user_instance.set_password(cleaned_data)
        user_instance.save()


class LoginForm(forms.Form):

    username = forms.CharField(
        validators=[RegexValidator(
            regex=validators.regex_sentences['email']
        )],
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Correo electrónico',
                'required': 'true',
            }
        ),
    )

    password = forms.CharField(
        validators=[validators.eval_blank],
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Contraseña',
                'required': 'true',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(
                username=username, password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    error_messages['invalid_login'],
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    error_messages['inactive_account']
                )
        return self.cleaned_data


class SignupForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Nombre'
            }
        ),
    )
    mother_last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Apellido materno'
            }
        ),
    )
    father_last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Apellido paterno'
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Correo electrónico',
            }
        ),
    )
    password_1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Contraseña'
            }
        ),
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Confirmar Contraseña'
            }
        ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Teléfono'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages
            self.fields[field].validators = [validators.eval_blank]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return validators.eval_unique(email, CoolUser, 'email', 'email')

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        return validators.eval_matching(password_1, password_2)

    def save(self):
        cleaned_data = super(SignupForm, self).clean()

        user = CoolUser(
            email=cleaned_data.get('email'),
            first_name=cleaned_data.get('name'),
            mother_last_name=cleaned_data.get('mother_last_name'),
            father_last_name=cleaned_data.get('father_last_name'),
            user_type='client',
            is_active=False,
        )

        user.set_password(cleaned_data.get('password_2'))

        user.save()

        client = Client(
            user=user,
            user_type='User type 1',
            contact_number=cleaned_data.get('phone'))
        client.save()

        self.user_cache = user


class UpdatePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Contraseña actual'
            }
        ),
    )
    new_password_1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Contraseña nueva'
            }
        ),
    )
    new_password_2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'emma-input',
                'placeholder': 'Confirmar'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True
            self.fields[field].error_messages = error_messages

    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        username = self.request.user.email
        return validators.eval_password(username, password)

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        new_password_1 = cleaned_data.get('new_password_1')
        new_password_2 = cleaned_data.get('new_password_2')
        if new_password_1 and new_password_2:
            return validators.eval_matching(new_password_1, new_password_2)

    def save(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        user_instance = self.request.user
        user_instance.set_password(cleaned_data)
        user_instance.save()