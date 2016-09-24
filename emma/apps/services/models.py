#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey

from emma.apps.adults.models import Adult
from emma.apps.clients.models import Client
from emma.apps.emmas.models import Emma, EmmaCoordinator

from django.contrib.contenttypes.models import ContentType

DAYS = (
    (('monday'),('Lunes')),
    (('tuesday'),('Martes')),
    (('wednesday'),('Miercoles')),
    (('thurday'),('Jueves')),
    (('friday'),('Viernes')),
    (('saturday'),('Sabado')),
    (('sunday'),('Domingo')),
)


class Service(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=40,
        blank=False,
        null=False
    )
    max_weekly_sessions = models.IntegerField(
        blank=True,
        null=True
    )
    weekly_hours = models.IntegerField(
        blank=True,
        null=True
    )
    price = models.PositiveSmallIntegerField(
        _('Price'),
        blank=False,
        null=False
    )
    allows_workshops = models.BooleanField(
        _('Allows workshops'),
        default=False,
    )
    allows_activities = models.BooleanField(
        _('Allows activities'),
        default=False,
    )
    max_hours_per_month = models.IntegerField(
        _('Max hours per month'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

    def __unicode__(self):
        return "%s" % self.name


class Workshop(models.Model):
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


class Activity(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=40,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

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
        verbose_name=_('Plan'),
    )
    workshops = models.ManyToManyField(
        Workshop,
        verbose_name=_('Workshops'),
        blank=False,
    )
    service_days = models.TextField(
        _('Service Days'),
        blank=False,
        null=False,
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
        EmmaCoordinator,
        verbose_name=_('Cordinator'),
        related_name='cordinator',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Hired service')
        verbose_name_plural = _('Hired services')

    def __unicode__(self):
        return '%s - %s - %s' % (self.adult, self.service, self.workshops)


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


class ServiceDay(models.Model):
    day = models.CharField(
        blank=False,
        null=False,
        default="",
        choices=DAYS,
        max_length=30,
    )

    start_time = models.CharField(
        blank=False,
        null=False,
        default="",
        max_length=30,
    )

    duration = models.IntegerField(
        blank=False,
        null=False,
        default=1
    )

    limit = models.Q(app_label='services', model='workshop') | \
            models.Q(app_label='services', model='activity')

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('Workshop or Activity'),
        limit_choices_to=limit,
        null=True,
        blank=True,
    )

    object_id = models.PositiveIntegerField(
        verbose_name=_('Activity or workshop ID'),
        null=True,
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Service Days')
        verbose_name_plural = _('Service Days')

    def __unicode__(self):
        return self.get_day_display()


class ServiceContractProcess(models.Model):
    user = models.OneToOneField(
        Client,
        verbose_name=_('Client'),
        on_delete=models.CASCADE,
        primary_key=True
    )
    plan = models.ForeignKey(
        Service
    )
    service_days = models.ManyToManyField(ServiceDay)

    class Meta:
        verbose_name = _('Service contract process')
        verbose_name_plural = _('Service contract process')
