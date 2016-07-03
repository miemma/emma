#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.forms import AdultInfo
from emma.apps.adults.models import Adult
from emma.core.mixins import ClientRequiredMixin


class AdultInformation(ClientRequiredMixin, View):
    template_name = 'adults/adult_detail.html'

    def get(self, request, id, **kwargs):
        adultform = self.get_initial_adult_form(request,
                                                self.get_adult(request, id))
        ctx = {
            'adultform': adultform,
            'adult': self.get_adult(request, id)
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request, id, **kwargs):
        kwargs = {'request': request, 'adult_id':id}
        adultform = AdultInfo(request.POST, request.FILES, **kwargs)

        if adultform.is_valid():
            adultform.save()
            messages.info(self.request, 'User update')
            return redirect(reverse_lazy('adults:dashboard_adult',
                                         kwargs={'id':id}))
        else:
            ctx = {'adultform': adultform}
            return render(request, self.template_name, ctx)

    @staticmethod
    def get_initial_adult_form(request, adult):
        form = AdultInfo(
            initial={
                'first_name': adult.first_name,
                'last_name': adult.last_name,
                'birthday': adult.birthday,
                'street': adult.address.street,
                'num_ext': adult.address.outdoor_number,
                'num_int': adult.address.interior_number,
                'delegation': adult.address.municipality,
                'colony': adult.address.colony,
                'postal_code': adult.address.postal_code,
                'reference': adult.address.reference,
                'photo': adult.photo,
            }
        )
        return form

    @staticmethod
    def get_client(request):
        return request.user.client

    def get_adult(self, request, id):
        client = self.get_client(request)
        if not id:
            adult = Adult.objects.filter(responsable=client)[0]
        else:
            adult = get_object_or_404(Adult, responsable=client, id=id)

        return adult
