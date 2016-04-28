#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

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
