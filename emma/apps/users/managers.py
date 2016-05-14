#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import BaseUserManager


class CoolUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, user_type,
                     is_admin, is_superuser):
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')
        if not user_type:
            raise ValueError('The given user type must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
            is_admin=is_admin,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name,
                         user_type):

        return self._create_user(email, password, first_name, last_name,
                                 user_type, is_admin=True, is_superuser=True)

    def create_user(self, email, first_name, last_name, user_type,
                    password=None):

        return self._create_user(email, password, first_name, last_name,
                                 user_type, is_admin=False, is_superuser=False)
