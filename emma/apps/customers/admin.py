#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.ScheduledCall)
class ScheduledCallAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    pass