#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^cambiar-password/', view=views.ChangePasswordView.as_view(),
        name='change_password'),

    url(regex=r'^login/', view=views.LoginView.as_view(), name='login'),
    url(regex=r'^logout/', view=views.logout_view, name='logout'),
]