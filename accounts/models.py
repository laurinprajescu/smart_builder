# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractUser):
    
    
    def is_tradesman(self):
      stripe_id = models.CharField(max_length=40, default='')
      return True

    objects = AccountUserManager()
      
    

class TradesmanUser(User):
   
    stripe_id = models.CharField(max_length=40, default='')
    objects = AccountUserManager()
    def is_tradesman(self):
      return True
#     