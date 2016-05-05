#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Suscription)
class SuscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'id_customer', 'status', 'active')


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('suscription', 'date', 'movement')


@admin.register(models.Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('suscription', 'date', 'amount', 'status')