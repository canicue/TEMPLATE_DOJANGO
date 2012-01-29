import settings
if settings.DEBUG:
     from django.views.static import serve
     _media_url = settings.MEDIA_URL
     if _media_url.startswith('/'):
         _media_url = _media_url[1:]
         urlpatterns += patterns('',
                                 (r'^%s(?P<path>.*)$' % _media_url,
                                 serve,
                                 {'document_root': settings.MEDIA_ROOT}))
      	 del(_media_url, serve)
MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')
MEDIA_URL = '/media/'
os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')

