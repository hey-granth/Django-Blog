# Description: This file is used to create signals for the user model.

# post_save signal is sent by the User model when a user is created.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# receiver is a decorator that receives signals from the sender.
from django.dispatch import receiver
from .models import Profile

# This function is used to create a profile for the user when a user is created.
# the receiver receives the post_save signal sent by the user to create a profile for the user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # instance is the user object.
    # created is a boolean value that is true if the user is created.
    # **kwargs is used to accept any additional keyword arguments.
    if created:
        Profile.objects.create(user=instance)

# This function is used to save the profile for the user when a user is created.
# the receiver receives the post_save signal sent by the user to save a profile for the user.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()