#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.models import Adult
from emma.apps.services.models import HiredService
from emma.core.mixins import ClientRequiredMixin, GetAdultMixin


class MainEmmaView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'emmas/emma_detail.html'

    def get(self, request):
        service = HiredService.objects.get(adult=self.get_adult(request))
        emma = service.emma_assigned
        ctx = {
            'emma': emma,
            'adult': self.get_adult(request),
        }
        return TemplateResponse(request, self.template_name, ctx)


class SecondEmmaView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'emmas/emma_detail.html'

    def get(self, request):
        service = HiredService.objects.get(adult=self.get_adult(request))
        emma = service.emma_alternate
        ctx = {
            'emma': emma,
            'adult': self.get_adult(request),
        }
        return TemplateResponse(request, self.template_name, ctx)


class CoordinatorEmmaView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'emmas/emma_coordinator.html'

    def get(self, request):
        service = HiredService.objects.get(adult=self.get_adult(request))
        emma = service.emma_cordinator
        ctx = {
            'emma': emma,
            'adult': self.get_adult(request),
        }
        return TemplateResponse(request, self.template_name, ctx)