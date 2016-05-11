#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from pyExcelerator import *

from . import models


def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta

    wb = Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = []
    # write header row
    for field in opts.fields:
        ws0.write(0, col, field.name)
        field_names.append(field.name)
        col = col + 1

    row = 1
    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            val = unicode(getattr(obj, field)).strip()
            ws0.write(row, col, val)
            col = col + 1
        row = row + 1

    wb.save('/Users/mauriciodinki/Proyectos/emma/emma/emma/media/output.xls')
    response = HttpResponse(open('/Users/mauriciodinki/Proyectos/emma/emma/emma/media/output.xls','r').read(),
                            content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    return response

@admin.register(models.ScheduledCall)
class ScheduledCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_time', 'number')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source')