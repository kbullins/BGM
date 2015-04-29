from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^home', 'BGM.views.home', name='home'),
    url(r'^calendar', 'BGM.views.calendar', name='calendar'),
    url(r'^about', 'BGM.views.about', name='about'),
    url(r'^contact', 'BGM.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 
