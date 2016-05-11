#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls
from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('service', 'name')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.HiredService)
class HiredServiceAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
