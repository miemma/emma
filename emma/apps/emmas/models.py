#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class PotentialEmma(models.Model):
    first_name = models.CharField(
        _('First Name'),
        max_length=100,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=100,
        null=False,
        blank=False,
    )
    age = models.CharField(
        _('Age'),
        max_length=100,
        null=False,
        blank=False,
    )
    movile_phone = models.CharField(
        _('Movile phone'),
        max_length=100,
        null=False,
        blank=False,
    )
    phone = models.CharField(
        _('Phone'),
        max_length=100,
        null=False,
        blank=False,
    )
    school_grade = models.CharField(
        _('School grade'),
        max_length=100,
        null=False,
        blank=False,
    )
    address = models.TextField(
        _('Address'),
        null=False,
        blank=False,
    )
    how_met_emma = models.CharField(
        _('How met Emma'),
        max_length=100,
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
        return '%s %s' % (self.first_name, self.last_name)



class Emma(models.Model):
    id = models.BigIntegerField(
        _('ID'),
        auto_created=True,
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=False,
        null=False,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        primary_key=True,
    )

    phone = models.CharField(
        _('Phone'),
        max_length=30,
        blank=True,
        null=True,
    )

    birthday = models.DateField(
        _('Birthday'),
        blank=True,
        null=True
    )
    main_occupation = models.TextField(
        _('Main occupation'),
        blank=True,
        null=True,
    )

    general_description = models.TextField(
        _('General Description'),
        max_length=500,
        blank=True,
        null=True,
    )
    qualities = models.TextField(
        _('Qualities'),
        max_length=500,
        blank=True,
        null=True,
    )
    experience_with_seniors = models.TextField(
        _('Experience with Seniors'),
        max_length=500,
        blank=True,
        null=True,
    )
    characteristics = models.TextField(
        _('Characteristics'),
        max_length=500,
        blank=True,
        null=True,
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


class EmmaStudies(models.Model):
    emma = models.ForeignKey(
        Emma,
        verbose_name=_('Emma')
    )
    studie = models.CharField(
        _('Studie'),
        max_length=50,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Emma Studie')
        verbose_name_plural = _('Emma Studies')

    def __unicode__(self):
        return '%s %s' % (self.emma, self.studie)


class EmmaCertification(models.Model):
    emma = models.ForeignKey(
        Emma,
        verbose_name=_('Emma')
    )
    certification = models.CharField(
        _('Certification'),
        max_length=100,
        blank=False,
        null=False,
    )

    time = models.CharField(
        _('Time'),
        max_length=100,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Emma Certification')
        verbose_name_plural = _('Emma Certifications')

    def __unicode__(self):
        return '%s %s' % (self.emma, self.certification)


class EmmaHobbie(models.Model):
    emma = models.ForeignKey(
        Emma,
        verbose_name=_('Emma')
    )
    hobbie = models.TextField(
        _('Hobbie'),
        max_length=200,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Emma Hobbie')
        verbose_name_plural = _('Emma Hobbies')

    def __unicode__(self):
        return '%s %s' % (self.emma, self.hobbie)


class EmmaCoordinator(models.Model):
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
    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=False,
        null=False,
    )

    phone = models.CharField(
        _('Phone'),
        max_length=30,
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return '%s' % (self.user)

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(EmmaCoordinator, self).save(*args, **kwargs)
