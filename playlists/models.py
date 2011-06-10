from django.db import models

class Playlist(models.Model):
	pl_name = models.CharField(maxlength=200)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	date_edited = models.DateTimeField('date last edited', auto_now=True)

	class Admin:
		pass

class Song(models.Model):
	artist = models.CharField(maxlength=200)
	song_name = models.CharField('song name', maxlength=200)
	bpm = models.IntegerField(blank=True)
	length = models.DateTimeField('song length', blank=True)
	playlist = models.ManyToManyField('Playlist', blank=True)

	class Admin:
		pass	
