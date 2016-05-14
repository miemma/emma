#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls

from . import models


@admin.register(models.Adult)
class AdultAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'responsable')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
