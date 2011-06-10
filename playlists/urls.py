from django.conf.urls.defaults import *

urlpatterns = patterns('playlists.views',
    (r'^$', 'index'),
    (r'^list/(?P<playlist_id>\d+)/$', 'detail'),
    (r'^song/(?P<song_id>\d+)/$', 'song_detail'),
    (r'^add/list/$', 'add_playlist'),
    (r'^add/song/$', 'add_song'),
)
