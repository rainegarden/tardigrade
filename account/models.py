import uuid
from django.contrib.auth.models import User
from django.db import models


class pfp(models.Model):
    """
Profile picture model for storing user profile images
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_binary = models.BinaryField()
