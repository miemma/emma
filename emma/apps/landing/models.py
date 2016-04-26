#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Customer(models.Model):
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
    source = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __unicode__(self):
        return self.name

