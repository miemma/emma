#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import PasswordResetForm as PasswdForm
from django.contrib.auth.forms import SetPasswordForm as SetPasswdForm



class PasswordResetForm(PasswdForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-form-input emma-input',
                'placeholder': 'Correo electrónico'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class SetPasswordForm(SetPasswdForm):
    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-form-input emma-input',
                'placeholder': 'Nueva Contraseña'
            }
        ),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'passwd-form-input emma-input',
                'placeholder': 'Confirmar Contraseña'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)