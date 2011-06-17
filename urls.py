from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings


urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^playlists/', include('playlists.urls')),
	(r'^map/', include('map.urls')),
    (r'^$', 'apples.views.home'),
    

    # (r'^apples/', include('apples.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
