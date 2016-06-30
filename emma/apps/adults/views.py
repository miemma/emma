#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.models import Adult
from emma.core.mixins import ClientRequiredMixin


class AdultInformation(ClientRequiredMixin, View):
    template_name = 'adults/adult_detail.html'

    def get(self, request, id, **kwargs):
        client = request.user.client
        if not id:
            adult = Adult.objects.filter(responsable=client)
            ctx = {'adult': adult[0]}
        else:
            adult = get_object_or_404(Adult, responsable=client, id=id)
            ctx = {'adult': adult}
        if client.active_client:
            return TemplateResponse(request, self.template_name, ctx)
        else:
            return redirect(reverse_lazy('landing:date'))