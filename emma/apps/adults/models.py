#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from emma.apps.clients.models import Client
from emma.apps.doctors.models import Doctor


PERFIL = (
    (1, 'Educacional'),
    (2, 'Depresión'),
    (3, 'Aislamiento Social'),
    (4, 'Deterioro Cognitivo'),
)

SEX = (
    (1, 'Femenino'),
    (2, 'Masculino'),
)
class AdultAddress(models.Model):
    adult_name = models.CharField(
        _('Adult Name'),
        max_length=50,
        blank=False,
        null=False
    )
    street = models.CharField(
        _('Street'),
        max_length=50,
        blank=False,
        null=False
    )
    outdoor_number = models.CharField(
        _('Outdoor Number'),
        max_length=25,
        blank=False,
        null=False
    )
    interior_number = models.CharField(
        _('Interior Number'),
        max_length=50,
        blank=True,
        null=True
    )
    colony = models.CharField(
        _('Colony'),
        max_length=50,
        blank=False,
        null=False
    )
    postal_code = models.PositiveIntegerField(
        _('Postal Code'),
        blank=False,
        null=False
    )
    municipality = models.CharField(
        _('Municipality'),
        max_length=50,
        blank=False,
        null=False
    )
    city = models.CharField(
        _('City'),
        max_length=50,
        blank=False,
        null=False
    )
    state = models.CharField(
        _('State'),
        max_length=50,
        blank=False,
        null=False
    )
    reference = models.TextField(
        _('Reference'),
        blank=False,
        null=False
    )
    google_maps_link = models.TextField(
        _('Google Maps Link'),
        blank=False,
        null=False
    )


    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __unicode__(self):
        return 'Address - %s' % self.adult_name


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
        blank=True,
        null=True,
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
        blank=True,
        null=True,
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
        max_length=100,
        blank=True,
        null=True,
    )
    policy_number = models.CharField(
        _('Policy Number'),
        max_length=100,
        blank=True,
        null=True,
    )
    policy_expiration_date = models.DateField(
        _('Policy Experation Date'),
        blank=True,
        null=True,
    )
    has_social_security = models.BooleanField(
        _('Has Social Security'),
        default=True
    )
    social_security_number = models.CharField(
        _('Social Security Number'),
        max_length=100,
        blank=True,
        null=True,
    )
    doctor = models.ForeignKey(
        Doctor,
        verbose_name=_('Doctor')
    )
    diseases = models.TextField(
        _('Diseases'),
        blank=True,
        null=True,
    )
    current_medications = models.TextField(
        _('Current Medications'),
        blank=True,
        null=True,
    )
    drug_allergy = models.TextField(
        _('Drug Allergy'),
        blank=True,
        null=True,
    )
    food_allergy = models.TextField(
        _('Food Allergy'),
        blank=True,
        null=True,
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
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=25,
        blank=False,
        null=False,
    )
    photo = models.ImageField(
        _('Profile picture'),
        upload_to='emma_profile_pictures',
        null=True,
        blank=True
    )
    age = models.CharField(
        _('Age'),
        max_length=2,
        null=False,
        blank=False,
    )
    birthday = models.DateField(
        _('Birthday'),
        blank=True,
        null=True,
    )
    address = models.ForeignKey(
        AdultAddress,
        verbose_name=_('Address'),
        null=True,
    )
    responsable = models.ForeignKey(
        Client,
        verbose_name=_('Responsable'),
        null=True,
    )
    description = models.TextField(
        _('Description'),
        blank=False,
        null=False,
    )
    familiar_structure = models.TextField(
        _('Familiar Structure'),
        blank=False,
        null=False,
    )
    personality = models.TextField(
        _('Personality'),
        blank=False,
        null=False,
    )

    hobbie = models.TextField(
        _('Hobbie'),
        blank=True,
        null=True,
    )

    interest = models.TextField(
        _('Interest'),
        blank=True,
        null=True,
    )
    # medical_information = models.OneToOneField(
    #     MedicalInfo,
    #     verbose_name=_('Medical Information'),
    #     blank=True,
    #     null=True
    # )
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
