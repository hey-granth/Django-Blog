from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # OneToOneField: one user has one profile, one profile has one user
    # on_delete=models.CASCADE: if user is deleted, profile is deleted.

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # __str__ method is used to return a string representation of the object.
    def __str__(self):
        return f'{self.user.username} Profile'

    # Save method is used to resize the image before saving it.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)