#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Emma)
class EmmaAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'movile_phone', 'phone')

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Name'