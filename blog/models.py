from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE means that if the user is deleted, then the post will also be deleted.
    # models.PROTECT means that if the user is deleted, then the post will not be deleted.
    # models.SET_NULL means that if the user is deleted, then the post will not be deleted, but the author will be set to NULL.


    def __str__(self):
        return self.title