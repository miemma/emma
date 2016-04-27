#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
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


class Client(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Address)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

