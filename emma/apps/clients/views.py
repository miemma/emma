#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.xauth.forms import UpdatePasswordForm
from emma.core.mixins import ClientRequiredMixin


class ClientDetailView(ClientRequiredMixin, View):
    template_name = 'clients/client_detail.html'
    form_class = UpdatePasswordForm

    def get(self, request, **kwargs):
        form = self.form_class()
        ctx = {'form':form}
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        kwargs = {'request':request}
        form = self.form_class(request.POST, **kwargs)
        if form.is_valid():
            form.save()
            ctx = {'form': self.form_class(), 'success': 'La contraseña se actualizo correctamente'}
            return TemplateResponse(request, self.template_name, ctx)
        else:
            ctx = {'form': form}
            return TemplateResponse(request, self.template_name, ctx)