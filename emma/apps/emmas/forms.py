#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.core.files.images import get_image_dimensions


from emma.apps.emmas.models import Emma


class EmmaCreationForm(forms.ModelForm):
    class Meta:
        model = Emma
        fields = '__all__'

    def clean_profile_picture(self):
        picture = self.cleaned_data.get("profile_picture")
        if hasattr(picture,'._size'):
            if picture._size > 5*1024*1024:
                raise forms.ValidationError(
                    "The image max size is 5MB")
        return picture