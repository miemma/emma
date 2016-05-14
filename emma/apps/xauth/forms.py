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
from emma.core.utils import generate_random_username


class PasswordResetRequestForm(PasswdForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-reset-req-form-input emma-input',
                'placeholder': 'Correo electrónico'
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
        new_password_1 = cleaned_data.get('new_password_1', '')
        new_password_2 = cleaned_data.get('new_password_2', '')
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
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Apellidos'
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

        user = CoolUser.objects.create_user(
            username=generate_random_username(),
            email=cleaned_data.get('email'),
            password=cleaned_data.get('password_2'),
        )
        user.first_name = cleaned_data.get('name')
        user.last_name = cleaned_data.get('last_name')

        user.save()

        client = Client(user=user, change_password=True)
        client.save()

        self.user_cache = authenticate(
            username=cleaned_data.get('email'),
            password=cleaned_data.get("password_2")
        )