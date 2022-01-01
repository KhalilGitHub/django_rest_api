from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import  PhoneNumberField
from apps.common.models import TimeStampedUUIDMpdel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMELE = "Female", _("Female")
    OTHER = "Other", _("Other")

class Profile(TimeStampedUUIDMpdel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+23566200135")
    about_me = models.TextField(verbose_name=_("About me"), default="Say Something about yourself")
    licence = models.CharField(verbose_name=_("Django Rest API Licence"), max_length=40, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Select photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Select a Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="TCD", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), default="Ndjamena", blank=False, null=False, max_length=80)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to Buy Property ? "))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to Sell Property ? "))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you Agent ? "))
    Top_agent = models.BooleanField(verbose_name=_("To Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
