#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import View, TemplateView

from emma.apps.services.models import HiredService
from emma.core.mixins import ClientRequiredMixin, GetAdultMixin


class MainEmmaView(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'emmas/emma_detail.html'

    def get(self, request):
        service = HiredService.objects.get(adult=self.get_adult(request))
        emma = service.emma_assigned
        if emma:
            ctx = {
                'emma': emma,
                'adult': self.get_adult(request),
            }
            return TemplateResponse(request, self.template_name, ctx)
        else:
            return redirect(reverse_lazy('emmas:dashboard_standby_emma'))


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


class StandEmma(ClientRequiredMixin, TemplateView):
    template_name = 'emmas/stand_emma.html'
