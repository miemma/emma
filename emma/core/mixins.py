#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

from emma.apps.adults.models import Adult
from emma.apps.clients.models import Client
from emma.apps.suscriptions.models import Suscription


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
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
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


class ClientRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
    def dispatch(self, request, *args, **kwargs):
        try:
            Client.objects.get(user=request.user)
            return super(ClientRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)
        except Client.DoesNotExist:
            raise PermissionDenied


class AdminRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
    def dispatch(self, request, *args, **kwargs):
        print 'validate'
        #Client.objects.get(user=request.user)
        if request.user.is_superuser:
            return super(AdminRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)
        else:
            raise PermissionDenied

class ActiveClientRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
    def dispatch(self, request, *args, **kwargs):
        try:
            Client.objects.get(user=request.user, user_type='User type 2')
            return super(ActiveClientRequiredMixin, self).dispatch(
                request, *args, **kwargs)
        except Client.DoesNotExist:
            raise PermissionDenied

class ActiveSuscriptionRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
    def dispatch(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(user=request.user, active_client=True)
            try:
                Suscription.objects.get(client=client, is_active=True)
                return super(ActiveSuscriptionRequiredMixin, self).dispatch(
                    request, *args, **kwargs)
            except Suscription.DoesNotExist:
                raise PermissionDenied
        except Client.DoesNotExist:
            raise PermissionDenied


class GetAdultMixin(object):
    def get_adult(self, request):
        client = request.user.client
        if client.user_type != 'User type 3':
            adult = None
        else:
            if not 'adult_id' in request.session:
                adult = Adult.objects.filter(responsable=client)[0]
            else:
                adult = get_object_or_404(Adult, responsable=client, id=id)

        return adult
