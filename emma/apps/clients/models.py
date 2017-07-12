#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# SOURCE = (
#     (1, 'Contacto'),
#     (2, 'Página'),
#     (3, 'Red social'),
#     (4, 'Otro'),
# )

class ClientAddress(models.Model):
    client_name = models.CharField(
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


    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __unicode__(self):
        return 'Address - %s' % self.client_name


class Client(models.Model):
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
    contact_number = models.CharField(
        _('Contact Number'),
        max_length=20,
        blank=True,
        null=True
    )
    user_type = models.CharField(
        _('User type'),
        max_length=30,
        choices=(
            ('User type 1', 'User type 1'),
            ('User type 2', 'User type 2'),
            ('User type 3', 'User type 3'),
        )
    )
    first_time_dashboard = models.BooleanField(
        _('First time dashboard'),
        default=True,
    )

    address = models.ForeignKey(
        ClientAddress,
        verbose_name=_('Address'),
        null=True,
    )

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __unicode__(self):
        return '%s' % (self.user)

    def save(self, *args, **kwargs):
        parent_id = self.user.id
        self.id = parent_id
        super(Client, self).save(*args, **kwargs)


class PotentialClient(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=55,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        _('Email'),
        blank=False,
        null=False
    )

    phone = models.CharField(
        _('Phone'),
        max_length=20,
        null=True,
        blank=True,
    )

    description = models.CharField(
        _('Description'),
        max_length=300,
        blank=True,
        null=True,
    )

    kin = models.CharField(
        _('Kin'),
        max_length=100,
        blank=True,
        null=True,
    )
    source = models.CharField(
        _('Source'),
        max_length=55,
        blank=False,
        null=False,
    )

    creation_date = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = _('Potential client')
        verbose_name_plural = _('Potential clients')

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)


class ContractProcess(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name=_('Client')
    )
    id_service = models.IntegerField(
        _('ID Service'),
        null=True,
        blank=True,
    )
    workshop_list = models.CharField(
        _('Workshop List'),
        max_length=50,
        null=True,
        blank=True,
    )
    adult_address_id = models.IntegerField(
        _('ID Adult Address'),
        null=False,
        blank=False,
        default=0,
    )
    service_setup = models.BooleanField(
        _('Service Setup'),
        default=False
    )
    service_days = models.IntegerField(
        _('Service Days'),
        null=True,
        blank=False
    )
    adult_setup = models.BooleanField(
        _('Adult Setup'),
        default=False
    )