from django.db import models
from django.contrib.auth.models import User
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='media/album_covers/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    song_name = models.CharField(max_length=200, null=True, blank=True)
    audio_file = models.FileField(upload_to='songs/')
    duration = models.DurationField()

    def __str__(self):
        return self.song_name


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    favorites=models.ManyToManyField(Album,blank=True)
    def __str__(self):
        return self.user.username
