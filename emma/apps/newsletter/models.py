#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BlogSubscriber(models.Model):
    email = models.EmailField(
        _('Email'),
        max_length=50,
        blank = False,
        null = False
    )

    class Meta:
        verbose_name = 'Blog Subscriber'
        verbose_name_plural = 'Blog Subscribers'

    def __unicode__(self):
        return self.email
