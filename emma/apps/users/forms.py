#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

from emma.core import validators
from emma.core.messages import error_messages


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
                'placeholder': 'Correo',
            }
        ),
    )

    password = forms.CharField(
        validators=[validators.eval_blank],
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-form-input emma-input',
                'placeholder': 'Contraseña',
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
