#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.core.utils import export_as_xls

from . import models


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'cell_phone', 'home_phone')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']

    def get_full_name(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)

    get_full_name.short_description = 'Name'