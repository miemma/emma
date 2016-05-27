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
        max_length=40,
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
        max_length=40,
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
        blank=True,
        null=True
    )
    service = models.ForeignKey(
        Service,
        verbose_name=_('Hired Service'),
    )
    workshops = models.CharField(
        _('Workshops'),
        max_length=100,
        blank=False,
        null=False,
    )
    num_workshops = models.IntegerField(
        _('Number of Workshops'),
        blank=False,
        null=False,
    )
    start_date = models.CharField(
        _('Start date'),
        max_length=25,
        blank=False,
        null=False,
    )
    end_date = models.DateField(
        _('End date'),
        blank=True,
        null=True,
    )
    reference = models.CharField(
        _('Reference'),
        max_length=25,
        blank=False,
        null=False
    )
    service_day_1 = models.CharField(
        _('Day 1 of service'),
        max_length=25,
        blank=False,
        null=False
    )
    service_day_2 = models.CharField(
        _('Day 2 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    service_day_3 = models.CharField(
        _('Day 3 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    service_day_4 = models.CharField(
        _('Day 4 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    service_day_5 = models.CharField(
        _('Day 5 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    service_day_6 = models.CharField(
        _('Day 6 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    service_day_7 = models.CharField(
        _('Day 7 of service'),
        max_length=25,
        blank=True,
        null=True
    )
    emma_assigned = models.ForeignKey(
        Emma,
        verbose_name=_('Emma assigned'),
        related_name='emma_assigned',
        blank=True,
        null=True
    )
    emma_alternate = models.ForeignKey(
        Emma,
        verbose_name=_('Alternative Emma'),
        related_name='emma_alternate',
        blank=True,
        null=True
    )
    emma_cordinator = models.ForeignKey(
        Emma,
        verbose_name=_('Cordinator'),
        related_name='cordinator',
        blank=True,
        null=True
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
