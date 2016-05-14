#!/usr/bin/env python
# -*- coding: utf-8 -*-

TYPE_CHOICES = (
    ('emma', 'Emma'),
    ('client', 'Client'),
)

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
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

    def __unicode__(self):
        return ('%s %s') % (self.user.get_full_name(), self.postal_code)


class CoolUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, user_type, is_admin, is_superuser):
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')
        if not user_type:
            raise ValueError('The given user type must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
            is_admin=is_admin,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, user_type, password):

        return self._create_user(email, first_name, last_name, user_type,
                                 password, is_admin=True, is_superuser=True)

    def create_user(self, email, first_name, last_name, user_type, password=None):

        return self._create_user(email, first_name, last_name, user_type,
                                 password, is_admin=True, is_superuser=True)


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
        _('staff status'),
        default=False,
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
        return "%s - %s" % (self.get_full_name(), self.email)
