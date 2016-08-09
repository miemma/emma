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
    mother_last_name = models.CharField(
        _('Mother last name'),
        max_length=30,
        blank=False,
    )
    father_last_name = models.CharField(
        _('Father last name'),
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
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )
    join_date = models.DateField(
        _('Join Date'),
        auto_now_add=True
    )

    objects = CoolUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'mother_last_name', 'father_last_name', 'user_type']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = '%s %s %s' % (
            self.first_name, self.father_last_name, self.mother_last_name
        )
        return full_name.strip()

    def get_full_last_name(self):
        last__name = '%s %s' % (
            self.mother_last_name, self.father_last_name
        )
        return last__name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_superuser

    def __unicode__(self):
        return "%s - %s" % (self.email, self.get_full_name())
