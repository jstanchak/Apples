from django.db import models
from django.forms import ModelForm
from django.forms.models import modelformset_factory

class Playlist(models.Model):
	pl_name = models.CharField("Title",max_length=100)
	date_created = models.DateTimeField('date created')
	date_edited = models.DateTimeField('date last edited')
	
	def __unicode__(self):
		return u'%s' % (self.pl_name)
	



class PlaylistForm(ModelForm):
	class Meta:
		model = Playlist
		exclude = ('date_created', 'date_edited')
		

class Song(models.Model):
	artist = models.CharField(max_length=200)
	song_name = models.CharField('song name', max_length=200)
	bpm = models.IntegerField(null=True, blank=True)
	length = models.DateTimeField('song length', null=True, blank=True)
	playlist = models.ManyToManyField('Playlist', null=True, blank=True)


class SongForm(ModelForm):
	class Meta:
		model = Song

SongFormSet = modelformset_factory(Song, extra=15)
