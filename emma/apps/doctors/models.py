#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Doctor(models.Model):
    first_name = models.CharField(
        _('First name'),
        max_length=25,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=25,
        blank=False,
        null=False,
    )
    cell_phone = models.CharField(
        _('Cell Phone'),
        max_length=25,
        blank=False,
        null=False,
    )
    home_phone = models.CharField(
        _('Home Phone'),
        max_length=25,
        blank=True,
        null=True,
    )
    working_institution = models.CharField(
        _('Working Institution'),
        max_length=25,
        blank=True,
        null=True,
    )
    professional_id = models.CharField(
        _('Professional ID'),
        max_length=25,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
