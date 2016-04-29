#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator


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


class RequestFormMixin(object):
    """ Puts the request in the kwargs to acces it in other places """
    def get_form_kwargs(self):
        kwargs = super(RequestFormMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class LoginRequiredMixin(object):
    """ Login required in class based views """
    @method_decorator(login_required(login_url=reverse_lazy('users:login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)


class NextUrlMixin(object):
    """
        Allows to redirect to the url in the next value in url
        remember to add <input type="hidden" name="next" value="{{ next }}">
        in the form
    """
    def get_context_data(self, **kwargs):
        kwargs.setdefault('next', self.request.GET.get('next'))
        return super(NextUrlMixin, self).get_context_data(**kwargs)

    def get_success_url(self):
        if 'next' in self.request.POST:
            url = self.request.POST.get('next')
        else:
            url = self.success_url
        return url
