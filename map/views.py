# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import simplejson
from map.Foursquare import Foursquare
from map.GoogleMaps import gMaps 

from django.core import serializers


import urllib

@csrf_protect
def fsq_places(request):
    foursquare_venues = []
    ll_string = ''
    if request.method == 'POST':
        address = request.POST["post_address"]	
    	latlong = gMaps.get_latlong(address)
    	lat = latlong['results'][0]['geometry']['location']['lat']
    	lng = latlong['results'][0]['geometry']['location']['lng']
    	ll_string = '%s, %s' % (lat, lng)
    	foursquare_venues = Foursquare.get_venues(ll_string)
    content = dict(foursquare_venues = foursquare_venues, ll_string = ll_string)
    return render_to_response('map/foursquare_venues.html', content, context_instance=RequestContext(request))