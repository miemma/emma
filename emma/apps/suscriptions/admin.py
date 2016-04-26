#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Suscription)
class SuscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Charge)
class ChargeAdmin(admin.ModelAdmin):
    pass