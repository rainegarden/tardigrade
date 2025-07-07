from django.db import models

# Create your models here.

class Category(models.Model):
    # Relation stuff
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True)
    children = models.ManyToManyField('self', blank=True, related_name='parent')
    level = models.IntegerField(default=1)

    # Name, Logo
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
