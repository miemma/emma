#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.adults.models import Adult
from emma.apps.clients.models import Client
from emma.apps.emmas.models import Emma


class Service(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=25,
        blank=False,
        null=False
    )
    price = models.PositiveSmallIntegerField(
        _('Price'),
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __unicode__(self):
        return "%s" % self.name


class Workshop(models.Model):
    service = models.ForeignKey(
        Service,
        verbose_name=_('Service')
    )
    name = models.CharField(
        _('Name'),
        max_length=25,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Workshop')
        verbose_name_plural = _('Workshops')

    def __unicode__(self):
        return "%s" % self.name


class HiredService(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name=_('Client'),
        on_delete=models.CASCADE,
    )
    adult = models.ForeignKey(
        Adult,
        verbose_name=_('Adult'),
    )
    service = models.ForeignKey(
        Service,
        verbose_name=_('Hired Service'),
    )
    workshop = models.ForeignKey(
        Workshop,
        verbose_name=_('Workshop'),
    )
    hours_per_week = models.PositiveSmallIntegerField(
        _('Hours per week'),
        blank=False,
        null=False
    )
    start_date = models.DateField(
        _('Start date'),
        blank=False,
        null=False,
    )
    end_date = models.DateField(
        _('End date'),
        blank=False,
        null=False,
    )
    reference = models.CharField(
        _('Reference'),
        max_length=25,
        blank=False,
        null=False
    )
    frequency = models.CharField(
        _('Frecuency'),
        max_length=25,
        blank=False,
        null=False
    )
    emma_assigned = models.ForeignKey(
        Emma,
        verbose_name=_('Emma assigned'),
        related_name='emma_assigned'
    )
    emma_alternate = models.ForeignKey(
        Emma,
        verbose_name=_('Alternative Emma'),
        related_name='emma_alternate'
    )
    emma_cordinator = models.ForeignKey(
        Emma,
        verbose_name=_('Cordinator'),
        related_name='cordinator'
    )

    class Meta:
        verbose_name = _('Hired service')
        verbose_name_plural = _('Hired services')

    def __unicode__(self):
        return '%s - %s - %s' % (self.adult, self.service, self.workshop)


class ScheduledCall(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        _('Email'),
        max_length=100,
        blank=False,
        null=False,
    )
    date_time = models.CharField(
        _('Date and time'),
        max_length=20,
        blank=False,
        null=False,
    )
    number = models.BigIntegerField(
        _('Number'),
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Scheduled call')
        verbose_name_plural = _('Scheduled calls')

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)
