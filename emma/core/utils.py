#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.conf import settings

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
        subject, body, from_email, to_email
    )
    email_message.send()


def generate_random_username(length=16, chars=ascii_lowercase+digits,
                             split=4, delimiter='-'):
    username = ''.join([choice(chars) for i in range(length)])
    if split:
        username = delimiter.join([username[start:start+split] for start in range(0, len(username), split)])
    try:
        User.objects.get(username=username)
        return generate_random_username(
            length=length, chars=chars, split=split, delimiter=delimiter
        )
    except User.DoesNotExist:
        return username