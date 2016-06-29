#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.views.generic import View


class MainEmma(View):
    template_name = 'emmas/emma_detail.html'

    def get(self, request):
        return TemplateResponse(request, self.template_name)