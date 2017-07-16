#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.views.generic import View, TemplateView, FormView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

from emma.apps.users.models import CoolUser
from emma.core.mixins import NextUrlMixin, AuthRedirectMixin, \
    LoginRequiredMixin, RequestFormMixin
from emma.core.utils import send_email

from .forms import PasswordResetRequestForm, PasswordResetForm, \
    ChangePasswordForm, SignupForm, LoginForm


class ActivateAccount(View):
    template_name = 'xauth/active_account.html'
    def get(self, request, uidb64):
        uid = urlsafe_base64_decode(uidb64)
        try:
            user = CoolUser.objects.get(id=uid)
        except CoolUser.DoesNotExist:
            user = None

        if user is not None:
            if user.is_active:
                raise Http404
            else:
                user.is_active = True
                user.save()
                return TemplateResponse(self.request, self.template_name)
        else:
            raise Http404


class PasswordReset(View):
    template_name = 'xauth/password_reset.html'
    token_generator = default_token_generator
    set_password_form = PasswordResetForm
    post_reset_redirect = reverse_lazy('xauth:reset_password_done')
    extra_context = None
    User = None

    def get(self, request, uidb64, token):
        usermodel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = usermodel._default_manager.get(request=uid)
        except (TypeError, ValueError, OverflowError, usermodel.DoesNotExist):
            self.User = None

        if self.User is not None and \
                self.token_generator.check_token(self.User, token):
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
        usermodel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = usermodel._default_manager.get(request=uid)
        except (TypeError, ValueError, OverflowError, usermodel.DoesNotExist):
            self.User = None
        form = self.set_password_form(self.User, request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.post_reset_redirect)


class PasswordResetDone(TemplateView):
    template_name = 'xauth/password_reset_done.html'


class PasswordResetRequest(View):
    template_name = 'xauth/password_reset_request.html'
    from_email = "Emma - Notificaciones <postmaster@%s>" % (
        settings.MAILGUN_SERVER_NAME
    )
    email_template_name = 'email/password_reset_request.html'
    email_subject = 'email/subjects/password_reset_request.txt',
    form = PasswordResetRequestForm
    token_generator = default_token_generator
    success_url = reverse_lazy('xauth:reset_password_request_done')
    html_email_template_name = None
    extra_email_context = None

    def get(self, request):
        form = self.form()
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


class PasswordResetRequestDone(TemplateView):
    template_name = 'xauth/password_reset_request_done.html'


class LoginView(NextUrlMixin, AuthRedirectMixin, FormView):
    template_name = 'xauth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('clients:dashboard_welcome')

    def form_valid(self, form):
        login(self.request, form.user_cache)

        if not form.user_cache.is_superuser:
            print 'no es superusuario'
            return redirect('clients:dashboard_welcome')
        else:
            print 'es superusuario'
            return redirect('admins:dashboard_welcome')
        #return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


@login_required(login_url=reverse_lazy('xauth:login'))
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('landing:home'))


class SignupView(FormView):
    template_name = 'xauth/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('xauth:signup_success')

    def form_valid(self, form):
        form.save()
        uid = urlsafe_base64_encode(str(form.user_cache.id))
        current_site = get_current_site(self.request)
        domain = current_site.domain
        send_email(
            subject='email/subjects/notification_welcome.txt',
            body='email/notification_welcome.html',
            context={
                'uid':uid,
                'domain':domain,
                'name': form.user_cache.first_name,
            },
            to_email=[form.user_cache.email],
        )
        return super(SignupView, self).form_valid(form)


class SignupSuccessView(TemplateView):
    template_name = 'xauth/success_signup.html'


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'xauth/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('users:select_card')

    def form_valid(self, form):
        form.save()
        client = self.request.user.client
        client.change_password = True
        client.save()
        return super(ChangePasswordView, self).form_valid(form)
