#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
import datetime

register = template.Library()

@register.filter
def age(bday, d=None):
    print(bday)
    if d is None:
        d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))