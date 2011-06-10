from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from playlists.models import *


import datetime

def index(request):
	latest_playlists = Playlist.objects.all().order_by('-date_edited')[:10]
	all_songs = Song.objects.all().order_by('artist')
	return render_to_response('playlists/index.html', {'latest_playlists': 
latest_playlists, 'all_songs': all_songs})
	
def detail(request, playlist_id):
	return HttpResponse("You're looking at playlist %s." % playlist_id)

def song_detail(request, song_id):
	return HttpResponse("You're looking at song %s." % song_id)

def add_playlist(request):
	if request.method == 'POST':
		form = PlaylistForm(request.POST)
		if request.POST:
			pl_new = form.save(commit=False)
			pl_new.date_created = datetime.datetime.now()
			pl_new.date_edited = datetime.datetime.now()
			pl_new.save()
			return render_to_response('playlists/detail.html', {'playlist': pl_new})
		else:
			return HttpResponse("it didn't save!")
	else:
		form = PlaylistForm()
		return render_to_response('playlists/add_list.html',{'form':form}, context_instance=RequestContext(request))

def add_song(request):
	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/playlists/')
		else:
			return HttpResponse("it didn't save!")
	else:
		form = SongForm()
		return render_to_response('playlists/add_song.html',{'form':form}, context_instance=RequestContext(request))

