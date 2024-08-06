from django.db import models
from django.contrib.auth.models import User


class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Anime(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
