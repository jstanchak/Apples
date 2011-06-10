from django.http import HttpResponse
from django.shortcuts import render_to_response
from playlists.models import *

def index(request):
	latest_playlists = Playlist.objects.all().order_by('-date_edited')[:10]
	return render_to_response('playlists/index.html', {'lastest_playlists': 
latest_playlists})
	
def detail(request, playlist_id):
	return HttpResponse("You're looking at playlist %s." % playlist_id)

def song_detail(request, song_id):
	return HttpResponse("You're looking at song %s." % song_id)

def add_playlist(request):
	return HttpResponse("You're trying to add a playlist.")

def add_song(request):
	return HttpResponse("You're trying to add a song.")

