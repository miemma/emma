#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


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
    contact_number = models.CharField(
        _('Contact Number'),
        max_length=20,
        blank=True,
        null=True
    )
    active_client = models.BooleanField(
        _('Active client'),
        default=False
    )
    first_time_dashboard = models.BooleanField(
        _('First time dashboard'),
        default=True,
    )

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __unicode__(self):
        return '%s' % (self.user)

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(Client, self).save(*args, **kwargs)


class PotentialClient(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=55,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        _('Email'),
        blank=False,
        null=False
    )
    source = models.CharField(
        _('Source'),
        max_length=55,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Potential client')
        verbose_name_plural = _('Potential clients')

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)


class ContractProcess(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name=_('Client')
    )
    id_service = models.IntegerField(
        _('ID Service'),
        null=True,
        blank=True,
    )
    workshop_list = models.CharField(
        _('Workshop List'),
        max_length=50,
        null=True,
        blank=True,
    )
    adult_address_id = models.IntegerField(
        _('ID Adult Address'),
        null=False,
        blank=False,
        default=0,
    )
    service_setup = models.BooleanField(
        _('Service Setup'),
        default=False
    )
    service_days = models.IntegerField(
        _('Service Days'),
        null=True,
        blank=False
    )
    adult_setup = models.BooleanField(
        _('Adult Setup'),
        default=False
    )