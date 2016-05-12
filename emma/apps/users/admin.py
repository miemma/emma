#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from emma.core.utils import export_as_xls
from . import models


def user_unicode(self):
    return u'%s, %s' % (self.last_name, self.first_name)


class CustomUserAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff',
                    'is_active')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"

User.__unicode__ = user_unicode
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(models.Address)
class AddresseAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'postal_code')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'active_client', 'change_password')
    actions = [export_as_xls]
    export_as_xls.short_description = "Export selected objects to XLS"

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'
