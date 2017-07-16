from django.shortcuts import render
from emma.core.mixins import AdminRequiredMixin
from django.views.generic import View
from django.template.response import TemplateResponse
# Create your views here.


class WelcomeView(AdminRequiredMixin, View):
    def get(self, request, **kwargs):
        print 'resolve admin'
        return TemplateResponse(request, 'admins/welcome.html')
           