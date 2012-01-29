from django import http
from django.conf import settings
from django.core import urlresolvers
from django.shortcuts import get_object_or_404, redirect
from django.utils import simplejson
from django.utils.encoding import force_unicode
from yabl.authors.models import Author

class RESTResource(object):
    """
    Dispatches based on HTTP method.
    """
    # Possible methods; subclasses could override this.
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    
    def __call__(self, request, *args, **kwargs):
        callback = getattr(self, request.method, None)
        if callback:
            return callback(request, *args, **kwargs)
        else:
            allowed_methods = [m for m in self.methods if hasattr(self, m)]
            return http.HttpResponseNotAllowed(allowed_methods)

class AuthorResource(RESTResource):
    """
    Base class for all Author resources providing conversion between Author
    objects and simple flat dicts.
    """
    def format(self, author, full=False):
        """
        Convert from an Author object to a dict.
        """
        link = urlresolvers.reverse('api_author_detail', args=[author.pk])
        info = {
            'first_name': author.first_name,
            'last_name': author.last_name,
            'link': link,
        }
        if full:
            info['bio'] = author.bio
        return info
        
    def parse(self, d):
        """
        Convert from a dict to an Author object.
        """
        try:
            return Author(
                first_name=force_unicode(d['first_name']),
                last_name=force_unicode(d['last_name']),
                bio=force_unicode(d.get('bio', '')),
            )
        except (ValueError, KeyError, TypeError):
            return None

class AuthorList(AuthorResource):
    """
    The list of authors (e.g. /api/authors/). 
    """
    def GET(self, request):
        return JSONResponse([self.format(a) for a in Author.objects.all()])

    def POST(self, request):
        author = self.parse(simplejson.loads(request.raw_post_data))
        if not author:
            return http.HttpResponseBadRequest()
        
        author.save()
        response = http.HttpResponse(status=201) # HTTP 201 Created
        response['Location'] = urlresolvers.reverse('api_author_detail', args=[author.pk])
        return response

class AuthorDetail(AuthorResource):
    """
    Author detail view (e.g. /api/authors/{id}/).
    """
    def GET(self, request, id):
        a = get_object_or_404(Author, pk=id)
        return JSONResponse(self.format(a, full=True))
        
    def DELETE(self, request, id):
        try:
            Author.objects.get(pk=id).delete()
        except Author.DoesNotExist:
            pass
        return redirect('api_author_list')
        
    def PUT(self, request, id):
        author = self.parse(simplejson.loads(request.raw_post_data))
        if not author:
            return http.HttpResponseBadRequest()
        author.id = id
        author.save()
        return JSONResponse(self.format(author, full=True))

class JSONResponse(http.HttpResponse):
    def __init__(self, data):
        indent = 2 if settings.DEBUG else None
        mime = ("text/javascript" if settings.DEBUG 
                                  else "application/json")
        super(JSONResponse, self).__init__(
            content=simplejson.dumps(data, indent=indent),
            mimetype=mime,
        )
