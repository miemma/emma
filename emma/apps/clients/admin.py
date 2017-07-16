#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emma.apps.clients.forms import ClientCreationForm
from emma.core.utils import export_as_xls

from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientCreationForm
    list_display = ('id', 'user', 'get_email',)# 'user_type')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
    exclude = ['id']

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'


@admin.register(models.PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.ContractProcess)
class ContractProcessAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"
