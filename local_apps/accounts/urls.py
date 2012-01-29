from django.conf.urls.defaults import patterns


# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('local_apps.accounts.views',
 

                        (r'^$', 'login'),
                          (r'^logout/$', 'logout'),



                       )
