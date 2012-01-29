function listProperties(obj) { 
	   var propList = ""; 
	   for(var propName in obj) { 
	      if(typeof(obj[propName]) != "undefined") { 
	         propList += (propName + ", "); 
	      } 
	   } 
	   alert(propList); 
	} 