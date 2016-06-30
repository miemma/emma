#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls

from . import models


@admin.register(models.Adult)
class AdultAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'responsable')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.MedicalInfo)
class MedicalInfoAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'relation', 'cell_phone',
                                                           'home_phone')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.AdultAddress)
class AdultAddress(admin.ModelAdmin):
    list_display = ('id', 'street', 'postal_code')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
