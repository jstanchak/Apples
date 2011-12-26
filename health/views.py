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

from django.core import serializers


import urllib

@csrf_protect
def index(request):
    content = dict()
    return render_to_response('health/index.html', content, context_instance=RequestContext(request))