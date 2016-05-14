#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from emma.apps.clients.models import Client
from emma.apps.users.models import Address


class Adult(models.Model):
    name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    birthday = models.DateField(
        blank=False,
        null=False
    )
    marital_status = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    address = models.ForeignKey(
        Address,
        blank=True,
        null=True,

    )
    responsable = models.ForeignKey(Client)
    is_candidate = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Adult'
        verbose_name_plural = 'Adults'

    def __unicode__(self):
        return ('%s %s') % (self.name, self.last_name)