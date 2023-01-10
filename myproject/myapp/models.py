from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    episode = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
