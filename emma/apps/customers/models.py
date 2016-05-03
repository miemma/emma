#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class ScheduledCall(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        null=False,
    )
    date_time = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    number = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Scheduled call'
        verbose_name_plural = 'Scheduled calls'


class PotentialClient(models.Model):
    name = models.CharField(
        max_length=55,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False
    )

    source = models.CharField(
        max_length=55,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Potential client'
        verbose_name_plural = 'Potential clients'