#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


from emma.apps.users.models import Address


class Emma(models.Model):
    id = models.BigIntegerField(
        _('ID'),
        auto_created=True,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    birthday = models.DateField(
        _('Birthday'),
        null=False,
        blank=False,
    )
    movile_phone = models.PositiveIntegerField(
        _('Movile phone'),
        null=False,
        blank=False,
    )
    phone = models.PositiveIntegerField(
        _('Phone'),
        null=False,
        blank=False,
    )
    school_grade = models.CharField(
        _('School grade'),
        max_length=15,
        null=False,
        blank=False,
    )
    direction = models.ForeignKey(
        Address,
        verbose_name=_('Address'),
    )
    how_met_emma = models.CharField(
        _('How met Emma'),
        max_length=15,
        null=False,
        blank=False,
    )
    has_facebook = models.BooleanField(
        _('Has Facebook'),
        default=False,
    )
    has_smathphone = models.BooleanField(
        _('Has smathphone'),
        default=False,
    )

    class Meta:
        verbose_name = _('Emma')
        verbose_name_plural = _('Emmas')

    def __unicode__(self):
        return '%s' % self.user

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(Emma, self).save(*args, **kwargs)
