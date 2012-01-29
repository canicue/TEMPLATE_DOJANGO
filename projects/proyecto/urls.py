from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#
urlpatterns = patterns('',
	(r'^i18n/', include('django.conf.urls.i18n') ),
	(r'^admin/doc/', include('django.contrib.admindocs.urls') ), #esta va antes de admin
	(r'^accounts/', include('local_apps.accounts.urls') ),
	(r'^admin/', include(admin.site.urls)),
	(r'^$', 'local_apps.accounts.views.login' ),
	(r'^dojango/',include('dojango.urls')),
	url(r'^rosetta/', include('rosetta.urls')),
    url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$', 'chronograph.views.job_run', name="admin_chronograph_job_run"),
	
	
)

