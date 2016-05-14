#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.clients.models import Client


class Suscription(models.Model):
    id = models.BigIntegerField(
        _('ID'),
        auto_created=True,
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
    id_customer = models.CharField(
        _('Cuatomer ID'),
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
        return "%s - %s" % (self.client.user.email, self.client)

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
    date = models.DateTimeField(
        _('Creation date'),
        auto_now_add=True
    )
    movement = models.CharField(
        _('Movement'),
        max_length=200,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')

    def __unicode__(self):
        return "%s - %s" % (self.suscription, self.movement)

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