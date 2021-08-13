from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, default="Uncatigorized")
    release_date = models.DateField()

    def __str__(self):
        return self.title