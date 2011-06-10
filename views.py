from django.http import HttpResponse

def home(request):
	return HttpResponse('Hello, Chris! I <3 YOU!')
