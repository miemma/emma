#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from emma.core.mixins import RequestFormMixin

from emma.apps.users.forms import ChangePasswordForm


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)