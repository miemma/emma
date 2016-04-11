#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

error_messages = {
    'blank': _('This field can not be blank'),
    'unique': _("There is a %(model_name)s with this %(field_label)s already registred"),
    'mismatch': _('The data do not match'),
    'invalid_login': _('The username or password are incorrect'),
    'inactive_account': _('This account is inactive'),
    'incorrect_password': _('The password is incorrect'),
}

confirmation_messages = {
    'updated_user': _('Profile updated'),
}
