#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^recuperar-password/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        view=views.PasswordReset.as_view(),
        name='reset_password'),

    url(regex=r'^recuperar-password/enviado/$',
        view=views.PasswordResetRequestDone.as_view(),
        name='reset_password_request_done'),

    url(regex=r'^recuperar-password/hecho/$',
        view=views.PasswordResetDone.as_view(),
        name='reset_password_done'),

    url(regex=r'^recuperar-password/$',
        view=views.PasswordResetRequest.as_view(),
        name='reset_password_form'),

    url(regex=r'^login/$',
        view=views.LoginView.as_view(),
        name='login'),

    url(regex=r'^logout/$',
        view=views.logout_view,
        name='logout'),

    url(regex=r'^signup/$',
        view=views.SignupView.as_view(),
        name='signup'),

]
