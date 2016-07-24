#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from emma.apps.suscriptions.models import History


class HistoryFormAdmin(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'
        widgets = {
            'workshops': forms.CheckboxSelectMultiple(),
        }