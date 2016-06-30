#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.models import Adult
from emma.apps.services.models import HiredService
from emma.core.mixins import ClientRequiredMixin


class MainEmma(ClientRequiredMixin, View):
    template_name = 'emmas/emma_detail.html'

    def get(self, request):
        adult = Adult.objects.get(responsable=request.user.client)
        service = HiredService.objects.get(adult=adult)
        emma = service.emma_assigned
        ctx = {
            'emma': emma
        }
        return TemplateResponse(request, self.template_name, ctx)