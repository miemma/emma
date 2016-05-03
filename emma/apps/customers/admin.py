#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.ScheduledCall)
class ScheduledCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_time', 'number')


@admin.register(models.PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source')