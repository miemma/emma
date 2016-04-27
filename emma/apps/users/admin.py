#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Address)
class AddresseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass