#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source')