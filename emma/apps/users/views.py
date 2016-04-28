#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from emma.core.mixins import RequestFormMixin, AuthRedirectMixin

from emma.apps.users.forms import ChangePasswordForm, LoginForm


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)


class LoginView(AuthRedirectMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())
