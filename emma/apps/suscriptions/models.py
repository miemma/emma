#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.clients.models import Client
from emma.apps.services.models import Service, Workshop


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('reports', filename)


class Suscription(models.Model):
    id = models.BigIntegerField(
        _('ID'),
    )
    client = models.OneToOneField(
        Client,
        verbose_name=_('Client'),
        related_name='suscriptions',
        primary_key=True,
    )
    date = models.DateTimeField(
        _('Creation date'),
        auto_now_add=True
    )
    openpay_id = models.CharField(
        _('Openpay ID'),
        max_length=25,
        blank=False,
        null=False
    )
    status = models.CharField(
        _('Status'),
        max_length=25,
        blank=False,
        null=False
    )
    is_active = models.BooleanField(
        _('Active'),
        default=False
    )

    class Meta:
        verbose_name = _('Suscription')
        verbose_name_plural = _('Suscriptions')

    def __unicode__(self):
        return '%s' % self.client

    def save(self, *args, **kwargs):
        parent_id = self.client.id
        self.id = parent_id
        super(Suscription, self).save(*args, **kwargs)


class History(models.Model):
    suscription = models.ForeignKey(
        Suscription,
        verbose_name=_('Suscription'),
        related_name='movements'
    )
    date = models.DateField(
        _('Creation date'),
        blank=False,
        null=False
    )
    service = models.ForeignKey(
        Service,
        verbose_name='Service'
    )
    workshops = models.ManyToManyField(
        Workshop,
        verbose_name=_('Workshops'),
        blank=False,
    )
    comments = models.TextField(
        _('Comments'),
        blank=False,
        null=False
    )
    file = models.FileField(
        _('File'),
        blank=True,
        null=True,
        upload_to='reports',
    )

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')

    def __unicode__(self):
        return "%s - %s" % (self.suscription, self.suscription.client)


class Charge(models.Model):
    suscription = models.ForeignKey(
        Suscription,
        verbose_name=_('Suscription'),
        related_name='charges'
    )
    date = models.DateTimeField(
        _('Creation date'),
        auto_now_add=True
    )
    amount = models.FloatField(
        _('Amount'),
        blank=False,
        null=False,
        max_length=100000
    )
    status = models.CharField(
        _('Status'),
        max_length=25,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        _('Description'),
        max_length=30,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Charge')
        verbose_name_plural = _('Charges')

    def __unicode__(self):
        return "%s - %s" % (self.suscription, self.amount)
