#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.views.generic import FormView
from django.views.generic.edit import FormMixin

from emma.core.mixins import RequestFormMixin, AuthRedirectMixin, \
    LoginRequiredMixin, NextUrlMixin

from emma.apps.users.forms import ChangePasswordForm, LoginForm


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)


class LoginView(NextUrlMixin, AuthRedirectMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


@login_required(login_url=reverse_lazy('users:login'))
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('landing:home'))