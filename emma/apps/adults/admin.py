#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Adult)
class AdultAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'responsable')
