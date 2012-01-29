from django.db import connection
def sql_debug(f):
    '''
    Decorador útil para inspeccionar las sentencias SQL que se ejecutan en
    cada request.
    '''
    def inner(*args, **kwargs):
        r = f(*args, **kwargs)
        for d in connection.queries:
            print "time: %s\n sql:%s\n\n" % (d['time'], d['sql'])
        return r
    return inner
