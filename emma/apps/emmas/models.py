#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Emma(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(
        null=False,
        blank=False,
    )
    movile_phone = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    phone = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    school_grade = models.CharField(
        max_length=15,
        null=False,
        blank=False,
    )

    #direction = models.ForeignKey(Address)

    how_met_emma = models.CharField(
        max_length=15,
        null=False,
        blank=False,
    )

    has_facebook = models.BooleanField()

    has_smathphone = models.BooleanField()

    class Meta:
        verbose_name = 'Emma'
        verbose_name_plural = 'Emmas'

