#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.apps.emmas.forms import EmmaCreationForm
from emma.core.utils import export_as_xls

from . import models


@admin.register(models.PotentialEmma)
class PotentialEmmaAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'movile_phone', 'phone')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']

    def get_full_name(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)

    get_full_name.short_description = 'Name'


@admin.register(models.Emma)
class EmmaAdmin(admin.ModelAdmin):
    form = EmmaCreationForm
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']

@admin.register(models.EmmaCoordinator)
class EmmaAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']


@admin.register(models.EmmaStudies)
class EmmaStudiesAdmin(admin.ModelAdmin):
    list_display = ('emma', 'studie')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.EmmaCertification)
class EmmaCertificationAdmin(admin.ModelAdmin):
    list_display = ('emma', 'certification', 'time')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.EmmaHobbie)
class EmmaHobbieAdmin(admin.ModelAdmin):
    list_display = ('emma', 'hobbie')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"