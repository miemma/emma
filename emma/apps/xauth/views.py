#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.views.generic import View, TemplateView
from django.conf import settings


from .forms import PasswordResetForm, SetPasswordForm


class PasswordResetRequestDone(TemplateView):
    template_name = 'xauth/password_reset_request_done.html'


class PasswordResetRequestDone(TemplateView):
    template_name = 'xauth/password_reset_done.html'


class PasswordResetView(View):
    template_name = 'xauth/password_reset.html'
    token_generator = default_token_generator
    set_password_form = SetPasswordForm
    post_reset_redirect = reverse_lazy('landing:home')
    extra_context = None
    User = None

    def get(self, request, uidb64, token):
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            self.User = None

        if self.User is not None and self.token_generator.check_token(self.User,
                                                                      token):
            validlink = True
            title = 'Enter new password'
            form = self.set_password_form(self.User)
        else:
            validlink = False
            form = None
            title = 'Password reset unsuccessful'

        context = {
            'form': form,
            'title': title,
            'validlink': validlink,
        }

        return TemplateResponse(request, self.template_name, context)

    def post(self, request, uidb64, token):
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            self.User = None
        form = self.set_password_form(self.User, request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.post_reset_redirect)

class RequestPasswordResetForm(View):
    template_name = 'xauth/password_reset_form.html'
    from_email = "Notificaciones - Emma <postmaster@%s>" % (
        settings.MAILGUN_SERVER_NAME
    )
    email_template_name = 'email/password_reset_email.html'
    email_subject = 'email/subjects/password_reset_mail_subject.txt',
    form = PasswordResetForm
    token_generator = default_token_generator
    success_url = reverse_lazy('landing:home')
    html_email_template_name = None
    extra_email_context = None

    def get(self, request):
        form = PasswordResetForm()
        ctx = {
            'form': form,
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.email_subject,
                'request': request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
            return redirect(self.success_url)
