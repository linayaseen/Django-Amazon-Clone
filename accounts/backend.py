from typing import Any
from django.contrib.auth.backends import ModelBackend #default+
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.http import HttpRequest

class EmailOrUsernameLogin(ModelBackend):
    def authenticate(self, request, username=None,password=None,**kwargs):
        try:
            user=User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user=User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            
        if user.check_password(password):
            return user
        return None