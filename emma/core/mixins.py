#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy


class AuthRedirectMixin(object):
    """
    CBV mixin which redirect to another url if the user is authenticated
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args,
                                                      **kwargs)
