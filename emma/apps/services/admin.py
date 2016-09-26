#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.apps.services.forms import HiredServiceCreationForm
from emma.core.utils import export_as_xls
from . import models


@admin.register(models.ServiceDay)
class ServiceDayAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.HiredService)
class HiredServiceAdmin(admin.ModelAdmin):
    form = HiredServiceCreationForm
    list_display = ('adult', 'client', 'service',)
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.ScheduledCall)
class ScheduledCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_time', 'number')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.ServiceContractProcess)
class ServiceContractProcessAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')
