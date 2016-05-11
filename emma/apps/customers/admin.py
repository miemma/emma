#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls

from . import models


@admin.register(models.ScheduledCall)
class ScheduledCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_time', 'number')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"