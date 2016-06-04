#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import Context

from pyExcelerator import *

from random import choice
from string import ascii_lowercase, digits


DEFAULT_NOTIFICATION_EMAIL_FROM = "Emma - Notificaciones <postmaster@%s>" % (
    settings.MAILGUN_SERVER_NAME
)


def send_email(subject, body, to_email, context, from_email=None):
    if from_email is None:
        from_email = DEFAULT_NOTIFICATION_EMAIL_FROM

    subject = loader.render_to_string(subject, context)
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(body, context)
    email_message = EmailMultiAlternatives(
        subject, 'Text Content', from_email, to_email
    )
    email_message.attach_alternative(body, "text/html")
    email_message.send()
    print("Mensaje enviado")


def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta

    wb = Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = []
    # write header row
    for field in opts.fields:
        ws0.write(0, col, field.name)
        field_names.append(field.name)
        col = col + 1

    row = 1
    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            val = unicode(getattr(obj, field)).strip()
            ws0.write(row, col, val)
            col = col + 1
        row = row + 1

    wb.save('/tmp/output.xls')
    response = HttpResponse(open('/tmp/output.xls','r').read(),
                            content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    return response