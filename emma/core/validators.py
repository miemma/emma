#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.auth import authenticate
from django.utils.text import slugify

from .messages import error_messages


def eval_blank(data):
    """
    Function which evaluates that the data not be blank
    """
    if str(data).isspace():
        raise forms.ValidationError(error_messages['blank'])
    return data


def eval_matching(data_1, data_2):
    """
    Function which evaluates 2 data and verifies that are equal
    """
    if data_1 != data_2:
        raise forms.ValidationError(error_messages['mismatch'])
    return data_1 and data_2


def eval_password(username, password):
    """
    Function which evaluates a user, useful to validate risk actions
    """
    user_cache = authenticate(username=username, password=password)
    if user_cache is None:
        raise forms.ValidationError(error_messages['incorrect_password'])
    return username and password


def eval_unique(data, model, field, label):
    """
    Function which evaluates unique data in models, useful for slugs,
    usernames etc.
    """
    original = data
    model_name = (model._meta.verbose_name).lower()
    field_label = (model._meta.get_field(label).verbose_name).lower()
    lookup = '%s__iexact' % field
    if field == 'slug':
        data = slugify(data)
        lookup = field
    try:
        model.objects.get(**{lookup: data})
    except model.DoesNotExist:
        return original
    raise forms.ValidationError(
        error_messages['unique'],
        params={'model_name': model_name, 'field_label': field_label}
    )


# Regular Expresions to validate specific conditions
regex_sentences = {
    'numbres_and_letters_special': '^[a-zA-Z0-9_áéíóúñ\s]*$',
    'numbres_and_letters': '^[a-zA-Z0-9]*$',
    'email': '^[\w.@+-]+$',
    'zip_code': '^[0-9\-]*$',
}
