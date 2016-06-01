#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CoolUserManager

TYPE_CHOICES = (
    ('emma', 'Emma'),
    ('client', 'Client'),
)


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    street = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    outdoor_number = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    interior_number = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    colony = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    postal_code = models.PositiveIntegerField(
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
        return '%s %s' % (self.user.get_full_name(), self.postal_code)


class CoolUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        _('Email address'),
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        _('First name'),
        max_length=30,
        blank=False
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=30,
        blank=False,
    )
    user_type = models.CharField(
        _('User type'),
        max_length=20,
        choices=TYPE_CHOICES,
        default='client',
        blank=False,
    )
    is_admin = models.BooleanField(
        _('Staff'),
        default=False,
    )
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    objects = CoolUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return "%s - %s" % (self.email, self.get_full_name())
