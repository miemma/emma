#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$',
        view=views.HomeTemplateView.as_view(),
        name='home'),

    url(regex=r'^precios/$',
        view=views.ServicesTemplateView.as_view(),
        name='services'),

    url(regex=r'^faq/$',
        view=views.FAQTemplateView.as_view(),
        name='faq'),

    url(regex=r'^acerca/$',
        view=views.AboutTemplateView.as_view(),
        name='about'),

    url(regex=r'^aviso-de-privacidad/$',
        view=views.PrivacyTemplateView.as_view(),
        name='privacy'),

    url(regex=r'^hecho/$',
        view=views.SuccessTemplateView.as_view(),
        name='success'),

    url(regex=r'^pago-completado/$',
        view=views.SuccessPayTemplateView.as_view(),
        name='success_pay'),

    url(regex=r'^contratar/completado/$',
        view=views.SuccessContractTemplateView.as_view(),
        name='success_contract'),

    #url(regex=r'^unete/$', view=views.JoinEmailView.as_view(),
    #    name='join'),

    url(regex=r'^agendar/$', view=views.DateEmailView.as_view(),
        name='date'),

    url(regex=r'^quienes-somos/$',
        view=views.WhoTemplateView.as_view(),
        name='who'),

    url(regex=r'^enviar-mail/$',
        view=views.ContactEmailView.as_view(),
        name='send_contact_mail'),

    url(regex=r'^subscribe/$',
        view=views.NewsletterView.as_view(),
        name='subscribe'),

    url(regex=r'^gracias/$',
        view=views.AlternativeJoinEmmaView.as_view(),
        name='thanks'),

    url(regex=r'^reclutamiento-ok/$',
        view=views.ContactTeamEmmaView.as_view(),
        name='thanks'),

    url(regex=r'^agendar-home/$',
        view=views.HomeContactView.as_view(),
        name='home_call'),

    url(regex=r'^cita-home/$',
        view=views.HomeDateView.as_view(),
        name='home_date'),

    url(regex=r'^guia-balance-personal-y-cuidado-de-tus-padres/$',
        view=views.GuiaPersonal.as_view(),
        name='home_guia'),

    url(regex=r'^presentacion/$',
        view=views.PresentacionMiemma.as_view(),
        name='presentacion_miemma'),
]
