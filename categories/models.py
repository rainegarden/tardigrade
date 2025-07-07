from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    # Sharing, etc
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_categories", null=False)
    shared_with = models.ManyToManyField(User, related_name="shared_categories", blank=True)

    # Relation stuff
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    children = models.ManyToManyField('self', blank=True)
    level = models.IntegerField(default=1)

    # Name, Logo
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
