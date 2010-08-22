import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('converter.urls')),
	# Example:
	# (r'^project_template/', include('project_template.foo.urls')),
	#(r'^manage/doc/', include('django.contrib.admindocs.urls')),
	#(r'^manage/', include(admin.site.urls)),
	(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root':getattr(settings,'MEDIA_ROOT')}),	
	(r'^converted_docs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.curdir+'/converted_docs'}),
	#url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout')
)

# Generic Views
#urlpatterns += patterns('',
#	url(r'^$', direct_to_template, {'template': 'home.phtml'}, name='index'),
#)