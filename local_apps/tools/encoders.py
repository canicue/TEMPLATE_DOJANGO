import simplejson
import datetime
class JSONEncoder(simplejson.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, (datetime.date,datetime.datetime)):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            return simplejson.JSONEncoder.default(self, obj)