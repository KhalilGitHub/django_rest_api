import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_api.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile, User

logger = logging.getLogger(__name__)

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(User=instance)

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}' profile created")