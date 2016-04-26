#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HiredService)
class HiredServiceAdmin(admin.ModelAdmin):
    pass
