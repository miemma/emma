#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

error_messages = {
    'blank': _('El campo no puede estar en blanco'),
    'required': _('Este campo es requerido'),
    'unique': _("Este registro ya existe"),
    'mismatch': _('La información no coincide'),
    'invalid_login': _('El usuario o la contraseña son incorrectas'),
    'inactive_account': _('Esta cuenta esta inactiva'),
    'incorrect_password': _('La contraseña es incorrecta'),
    'invalid': _('El contenido no es valido'),
}

confirmation_messages = {
    'updated_user': _('Profile updated'),
}
