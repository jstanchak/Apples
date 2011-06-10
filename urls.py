from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^playlists/', include('playlists.urls')),
    (r'^$', 'apples.views.home'),
    

    # (r'^apples/', include('apples.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
