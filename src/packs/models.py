from django.db import models

class Pack(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField()
