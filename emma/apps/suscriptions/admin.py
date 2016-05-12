#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls
from . import models


@admin.register(models.Suscription)
class SuscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'id_customer', 'status', 'active')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('suscription', 'date', 'movement')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('suscription', 'date', 'amount', 'status')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"