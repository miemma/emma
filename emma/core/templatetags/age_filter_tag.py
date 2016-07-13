#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

import datetime

register = template.Library()

@register.filter
def age(bdays):
    if not isinstance(bdays, datetime.date):
        bday = datetime.datetime.strptime(bdays, "%Y-%m-%d")
    else:
        bday = bdays
    d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))