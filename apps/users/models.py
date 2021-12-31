import uuid
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=55)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=55)
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    date_joined = models.BooleanField(timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name",]      

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def __str_(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.username
 

