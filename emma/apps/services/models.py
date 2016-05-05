#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from emma.apps.emmas.models import Emma


class Service(models.Model):
    name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    price = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __unicode__(self):
        return "%s - %s" % (self.name, self.price)


class Workshop(models.Model):
    service = models.ForeignKey(Service)
    name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'

    def __unicode__(self):
        return "%s - %s" % (self.service.name, self.name)


class HiredService(models.Model):
    user = models.ForeignKey(User)
    #old_man = models.ForeignKey(OldMan)
    service = models.ForeignKey(Service)
    workshop = models.ForeignKey(Workshop)
    hours_per_week = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )
    start_date = models.DateField(
        blank=False,
        null=False,
    )
    end_date = models.DateField(
        blank=False,
        null=False,
    )
    reference = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    frequency = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    emma_assigned = models.ForeignKey(
        Emma,
        related_name='emma_assigned'
    )
    emma_alternate = models.ForeignKey(
        Emma,
        related_name='emma_alternate'
    )
    coordinator = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Hired service'
        verbose_name_plural = 'Hired services'
