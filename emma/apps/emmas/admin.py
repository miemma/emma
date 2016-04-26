#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Emma)
class EmmaAdmin(admin.ModelAdmin):
    pass