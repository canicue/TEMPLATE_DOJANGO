#This code fetches the file name stored in the database send to the simple json format
#Images are displayed in random way in a 5 place holder in the template
def getImages(request):
    from django.http import HttpResponse
    from django.utils import simplejson
    import random
    LAST_INDEX = -1
    NUMBER_OF_ADS = 5
    slide_show = << modelsName >> .objects.all()
    slide_show_randomIMG = [random.choice(slide_show).adspath.name.split('/')[LAST_INDEX] for i in range(NUMBER_OF_ADS)]    
    json = simplejson.dumps(slide_show_randomIMG)
    return HttpResponse(json, mimetype='application/javascript')

#Template Code
var $ = jQuery.noConflict();
$(document).ready(function() {    
    setTimer();
});

function setTimer() {
    // Call the gallery function to run the slideshow, 7000 = change to next image after 7 seconds
    setInterval('changeImage()', 7000);
}

function changeImage() {   
    $.getJSON("/getImages/",
    function(json) {                
            for (j=json.length - 1; j >= 0; j - -) {
                imagID="addImg" + (j + 1);                
                document.getElementById(imagID).src="/static/ads/" + json[j];                
            }        
        }
    );
}
