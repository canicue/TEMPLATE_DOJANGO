urls.py
== = 
# The main url to kick it all off:
(r'^massupdate/$', 'scents.massupdate.views.drawMassUpdatePage'),
# Called by Ajax:
url(r'^doit/$', 'scents.massupdate.views.doit', name="doit"),
# Called by Ajax to pull status:
url(r'^getCount/$', 'scents.massupdate.views.getCount', name="getcount"),
	

views.py
== = 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

import time

def drawMassUpdatePage(request):
	request.session['count'] = 0
	request.session['done'] = False
	request.session.modified = True # May not need this.
	return render_to_response("massupdate/testajax.html") # template at end

# Kicks off the update. After this starts jquery will call
# getCount periodically to 'pull' results.
def doit(request):
	# Do something long and slow
	for i in range(0, 5000):
		request.session['count'] = i
		request.session.save() # Had to do this to actually use the session in getCount.
		#time.sleep(2) # Can make it even slower with this.

	request.session['done'] = True
	
	# This one is talking to a different func in the js.
	return HttpResponse('All done.', mimetype='text/plain')

# This one is being pulled by $.ajax in the js.
def getCount(request):
	i = request.session.get('count', 0) # Fetch the count or 0
	isitdone = request.session.get('done', False) # Fetch the status or False
	if isitdone:
		# It's all finished, so send a flag.
		d = {"done":True}
		j = simplejson.dumps(d)
		return HttpResponse(j, mimetype='application/javascript')
	else:
		# It's busy, so send a flag and a count
		d = {"done":False, "count":i}
		j = simplejson.dumps(d)
		return HttpResponse(j, mimetype='application/javascript')
	
template: testajax.html
== = 
< html > 
< head > 
	< script type = "text/javascript" src = "/media/js/jquery/jquery-1.2.6.pack.js" ></ script > 
</ head > 
< body > 

< script type = "text/javascript" > 
$(document).ready(function() { 

		// The func that calls getCount
		function pull() {
		// I use $.ajax. getJSON seems to cache the last data on ie6. Firefox work tho.
		$.ajax ({
			type: "GET",
			url: "{% url getcount %}",
			dataType: "json",
			cache: false, // VITAL line: the getJON func does not prevent caching ! 
			success: updater // Call this func when we have some data
		})
		}

		// Func to use the data fetched
		function updater(data, success) {
			if (data) {
				// If done flag sent, say so.
				if (data.done) {
					txt="DONE";
				} else { 
					// We are busy, get the count and...
					txt=data.count;
					// set this to start again in 2 seconds:
					window.setTimeout(pull, 2000);
				}
				// Display out count / message
				$('#msg').text("SETTING TO:" + txt);
			}
		} // end updater

		// You can start it automagically like this:
		// $('#muffin').load("{% url doit %}");
		
		// Or with an anchor
		$("#go").click(function() {
				$(this).hide(); // Hide the anchor
				// Call doit func in Django view
				$('#muffin').load("{% url doit%}");
				// Start the pull function in 1 second:
				window.setTimeout(pull, 1000);
			});
	}); // end ready
</ script > 

< a id = "go" href = "#" > Start </ a > 
< div id = "muffin" > DARN </ div > 
< div id = "msg" style = "border:1px solid red;" > NUMBER </ div > 

</ body > 
</ html > 
