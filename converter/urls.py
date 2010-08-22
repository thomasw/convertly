from django.conf.urls.defaults import *

urlpatterns = patterns('converter.views',
	(r'^$', 'index'),
	(r'^download/(?P<job_id>[^\s]+)/$', 'download'),
	url(r'^upload/*$', 'upload', name='upload'),
)
