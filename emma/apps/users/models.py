#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User)
    street = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    outdoor_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )
    interior_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )
    colony = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    postal_code = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )
    municipality = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    city = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    state = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    reference = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __unicode__(self):
        return ('%s %s') % (self.user.get_full_name(), self.postal_code)


class Client(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(
        Address,
        blank=True,
        null=True
    )
    change_password = models.BooleanField(default=False)
    active_client = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __unicode__(self):
        return self.user.get_full_name()