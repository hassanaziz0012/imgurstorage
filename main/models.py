from django.db import models

# Create your models here.
class Image(models.Model):
    file = models.ImageField()