from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_superuser(sender, instance, created, **kwargs):
    """Creates a profile for the superuser and user when the user is created from raw SQL"""
    if created and (instance.is_superuser or kwargs.get('raw')):
        Profile.objects.create(user=instance)
