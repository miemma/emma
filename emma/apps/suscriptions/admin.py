#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.apps.suscriptions.forms import HistoryFormAdmin
from emma.core.utils import export_as_xls
from . import models


@admin.register(models.Suscription)
class SuscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'openpay_id', 'status', 'is_active')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    form = HistoryFormAdmin
    list_display = ('suscription', 'date',)
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('suscription', 'date', 'amount', 'status')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"