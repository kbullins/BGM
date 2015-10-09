from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .forms import ContactForm
from django.core.mail import send_mail

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def home(request):
    return render(request, 'index.html', {})

def calendar(request):
    return render(request, 'calendar.html', {})

def about(request):
    return render(request, 'about.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})
	
def officers(request):
	return render(request, 'officers.html', {})

def bchamp(request):
	return render(request, 'bchamp.html', {})
	
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
	if form.is_valid():
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		sender = form.cleaned_data['sender']
		cc_myself = form.cleaned_data['cc_myself']
	
		recipients = ['info@example.com']
		if cc_myself:
			recipients.append(sender)
	
		from django.core.mail import send_mail
		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect('contact.html') # Redirect after POST

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
		
	return render(request, 'contact.html', {'form': form})

			