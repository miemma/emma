#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User

from emma.core.utils import export_as_xls
from . import models


def user_unicode(self):
    return '%s %s' % (self.first_name, self.last_name)

User.__unicode__ = user_unicode

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_staff')
    ordering = ('-date_joined',)

    def full_name(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)


@admin.register(models.Address)
class AddresseAdmin(admin.ModelAdmin):
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'active_client', 'change_password')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"