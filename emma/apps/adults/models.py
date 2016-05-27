#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.clients.models import Client
from emma.apps.users.models import Address


MARITAL_CHOICES = (
    ('married', _('Married')),
    ('widowed', _('Widowed')),
    ('divorced', _('Divorced')),
    ('separated', _('Separated')),
    ('single', _('Single')),
)


class Adult(models.Model):
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
    birthday = models.CharField(
        _('Birthday'),
        max_length=20,
        blank=False,
        null=False,
    )
    marital_status = models.CharField(
        _('Marital status'),
        max_length=25,
        blank=True,
        null=True,
        choices=MARITAL_CHOICES
    )
    address = models.ForeignKey(
        Address,
        verbose_name=_('Address'),
        blank=True,
        null=True,

    )
    responsable = models.ForeignKey(
        Client,
        verbose_name=_('Responsable'),
    )
    is_candidate = models.BooleanField(
        _('Candidate'),
        default=False,
    )

    class Meta:
        verbose_name = _('Adult')
        verbose_name_plural = _('Adults')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
