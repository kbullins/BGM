from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def home(request):
	if request.user.is_authenticated():
		# Do something for authenticated users.
		return render(request, 'index.html', {})
	else:
		# Do something for anonymous users.
		return render(request, 'index.html', {})

def calendar(request):
    return render(request, 'calendar.html', {})

def about(request):
    return render(request, 'about.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})
	
def officers(request):
	return render(request, 'officers.html', {})

def bcourt(request):
	return render(request, 'bcourt.html', {})
	
def armouredcombat(request):
    return render(request, 'armouredcombat.html', {})

def rapiercombat(request):
    return render(request, 'rapiercombat.html', {})

def artsciences(request):
    return render(request, 'artsciences.html', {})
	
def scriptorium(request):
	return render(request, 'scriptorium.html', {})

def meeting(request):
	return render(request, 'meeting.html', {})

def archery(request):
	return render(request, 'archery.html', {})
	
def contact(request):	
	return render(request, 'contact.html', {})
	
def newsletter(request):	
	return render(request, 'newsletter.html', {})

			