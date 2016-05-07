#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        view=views.PasswordResetView.as_view(),
        name='reset_password'),

    url(regex=r'^recuperar-password/',
        view=views.RequestPasswordResetForm.as_view(),
        name='reset_password_form'),

]
