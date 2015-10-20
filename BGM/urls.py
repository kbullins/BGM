from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'BGM.views.index', name='index'),
    url(r'^home', 'BGM.views.home', name='home'),
    url(r'^calendar', 'BGM.views.calendar', name='calendar'),
	url(r'^officers', 'BGM.views.officers', name='officers'),
	url(r'^bcourt', 'BGM.views.bcourt', name='bcourt'),
    url(r'^about', 'BGM.views.about', name='about'),
    url(r'^contact/$', 'BGM.views.contact', name='contact'),
	url(r'^thankyou/', 'BGM.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
	#Authentication Pages
	url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
	#Activities Pages
    url(r'^armouredcombat/$', 'BGM.views.armouredcombat', name='armouredcombat'),
	url(r'^rapiercombat/$', 'BGM.views.rapiercombat', name='rapiercombat'),
	url(r'^artsciences/$', 'BGM.views.artsciences', name='artsciences'),
	url(r'^scriptorium/$', 'BGM.views.scriptorium', name='scriptorium'),
	url(r'^meeting/$', 'BGM.views.meeting', name='meeting'),
	url(r'^archery/$', 'BGM.views.archery', name='archery'),
	url(r'^newsletter/$', 'BGM.views.newsletter', name='newsletter'),
) 
