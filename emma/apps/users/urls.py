#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^cambiar-password/', view=views.ChangePasswordView.as_view(),
        name='change_password'),
]