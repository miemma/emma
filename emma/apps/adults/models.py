#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.clients.models import Client
from emma.apps.doctors.models import Doctor


class AdultAddress(models.Model):
    street = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    outdoor_number = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    interior_number = models.CharField(
        max_length=25,
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
        return '%s' % self.postal_code


class EmergencyContact(models.Model):
    full_name = models.CharField(
        _('First name'),
        max_length=25,
        blank=False,
        null=False,
    )

    relation = models.CharField(
        _('Relation'),
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
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Emergency Contact')
        verbose_name_plural = _('Emergency Contacts')

    def __unicode__(self):
        return self.full_name


class MedicalInfo(models.Model):
    adult_name = models.CharField(
        _('Adult Full Name'),
        max_length=50,
        blank=False,
        null=False,
    )
    blood_type = models.CharField(
        _('Blood Type'),
        max_length=25,
        blank=False,
        null=False,
    )
    emergency_contact_1 = models.ForeignKey(
        EmergencyContact,
        verbose_name='Emergency Contact #1',
        related_name='emergency_contact_1'
    )
    emergency_contact_2 = models.ForeignKey(
        EmergencyContact,
        verbose_name='Emergency Contact #2',
        related_name='emergency_contact_2'
    )
    hospital_preferably = models.CharField(
        _('Hospital Preferably'),
        max_length=25,
        blank=False,
        null=False,
    )
    knows_pda = models.BooleanField(
        _('Knows PDA'),
        default=False
    )
    exercise_pda = models.BooleanField(
        _('Exercise PDA'),
        default=False
    )
    has_medical_insurance = models.BooleanField(
        _('Has Medical Insurance'),
        default=False,
    )
    insurance_company = models.CharField(
        _('Insurance Company'),
        max_length=25,
        blank=False,
        null=False,
    )
    policy_number = models.CharField(
        _('Insurance Company'),
        max_length=25,
        blank=False,
        null=False,
    )
    policy_expiration_date = models.DateField(
        _('Policy Experation Date'),
        blank=False,
        null=False,
    )
    has_social_security = models.BooleanField(
        _('Has Social Security'),
        blank=False,
        null=False,
    )
    social_security_number = models.CharField(
        _('Social Security Number'),
        max_length=25,
        blank=False,
        null=False,
    )
    doctor = models.ForeignKey(
        Doctor,
        verbose_name=_('Doctor')
    )
    diseases = models.TextField(
        _('Diseases'),
        blank=False,
        null=False,
    )
    current_medications = models.TextField(
        _('Current Medications'),
        blank=False,
        null=False,
    )
    drug_allergy = models.TextField(
        _('Drug Allergy'),
        blank=False,
        null=False,
    )
    food_allergy = models.TextField(
        _('Food Allergy'),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Medical Information')
        verbose_name_plural = _('Medical Information')

    def __unicode__(self):
        return 'Medical Information - %s' % self.adult_name


class Adult(models.Model):
    first_name = models.CharField(
        _('First name'),
        max_length=25,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=25,
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        _('Profile picture'),
        upload_to='emma_profile_pictures',
        null=True,
        blank=True
    )
    birthday = models.DateField(
        _('Birthday'),
        blank=True,
        null=True,
    )
    address = models.ForeignKey(
        AdultAddress,
        verbose_name=_('Address'),
        blank=True,
        null=True,

    )
    responsable = models.ForeignKey(
        Client,
        verbose_name=_('Responsable'),
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True,
    )
    familiar_structure = models.TextField(
        _('Familiar Structure'),
        blank=True,
        null=True,
    )
    personality = models.TextField(
        _('Personality'),
        blank=True,
        null=True,
    )
    medical_information = models.OneToOneField(
        MedicalInfo,
        verbose_name=_('Medical Information'),
        null=True,
        blank=True,
    )
    is_candidate = models.BooleanField(
        _('Candidate'),
        default=True,
    )

    class Meta:
        verbose_name = _('Adult')
        verbose_name_plural = _('Adults')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class AdultHobbie(models.Model):
    adult = models.ForeignKey(
        Adult,
        verbose_name=_('Adult')
    )

    hobbie = models.TextField(
        _('Hobbie'),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Adult Hobbie')
        verbose_name_plural = _('Adult Hobbie')

    def __unicode__(self):
        return '%s %s' % (self.adult, self.hobbie)
