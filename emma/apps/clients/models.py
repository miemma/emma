#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from emma.apps.users.models import Address


class Client(models.Model):
    id = models.BigIntegerField(
        _('ID'),
        auto_created=True,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.ForeignKey(
        Address,
        verbose_name=_('Address'),
        blank=True,
        null=True,
    )
    change_password = models.BooleanField(
        _('Change password'),
        default=False
    )
    active_client = models.BooleanField(
        _('Active client'),
        default=False
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __unicode__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(Client, self).save(*args, **kwargs)


class PotentialClient(models.Model):
    name = models.CharField(
        max_length=55,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False
    )

    source = models.CharField(
        max_length=55,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Potential client'
        verbose_name_plural = 'Potential clients'

    def __unicode__(self):
        return ('%s - %s') % (self.name, self.email)