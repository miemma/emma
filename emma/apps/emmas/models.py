#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class PotentialEmma(models.Model):
    first_name = models.CharField(
        _('First Name'),
        max_length=25,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=25,
        null=False,
        blank=False,
    )
    age = models.CharField(
        _('Age'),
        max_length=10,
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
    address = models.CharField(
        _('Address'),
        max_length=100,
        null=False,
        blank=False,
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
        verbose_name = _('Potential Emma')
        verbose_name_plural = _('Potential Emmas')

    def __unicode__(self):
        return '%s' % self.user

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(PotentialEmma, self).save(*args, **kwargs)


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
        blank=False,
        null=False
    )
    main_occupation = models.CharField(
        _('Main occupation'),
        max_length=30,
        blank=False,
        null=False,
    )

    general_description = models.CharField(
        _('General Description'),
        max_length=30,
        blank=False,
        null=False,
    )
    qualities = models.CharField(
        _('Qualities'),
        max_length=50,
        blank=False,
        null=False,
    )
    experience_with_seniors = models.CharField(
        _('Experience with Seniors'),
        max_length=50,
        blank=False,
        null=False,
    )
    characteristics = models.CharField(
        _('Characteristics'),
        max_length=50,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Emma')
        verbose_name_plural = _('Emmas')

    def __unicode__(self):
        return '%s' % (self.user)

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(Emma, self).save(*args, **kwargs)
