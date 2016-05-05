#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from emma.apps.users.models import Client


class Suscription(models.Model):
    user = models.ForeignKey(
        Client,
        related_name='suscriptions'
    )
    date = models.DateTimeField(auto_now_add=True)
    id_customer = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    status = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Suscription'
        verbose_name_plural = 'Suscriptions'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.status)


class History(models.Model):
    suscription = models.ForeignKey(
        Suscription,
        related_name='movements'
    )
    date = models.DateTimeField(auto_now_add=True)
    movement = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'

    def __unicode__(self):
        return "%s - %s" % (self.suscription, self.movement)

class Charge(models.Model):
    suscription = models.ForeignKey(
        Suscription,
        related_name='charges'
    )
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(
        blank=False,
        null=False,
        max_length=100000
    )
    status = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        max_length=30,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Charge'
        verbose_name_plural = "Charges"

    def __unicode__(self):
        return "%s - %s" % (self.suscription, self.amount)