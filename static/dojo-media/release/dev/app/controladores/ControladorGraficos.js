dojo.provide("desktop.controladores.ControladorGraficos");
dojo.require("dijit.dijit");
dojo.require("dijit.Dialog");
dojo.require("dojo.io.iframe");
dojo.require("dojox.layout.FloatingPane");
dojo.require("dojox.charting.Chart");
dojo.require("dojox.charting.themes.Shrooms")

dojo.declare("desktop.controladores.ControladorGraficos",[],{

  

    constructor:function()
    {
        dojo.global.controladorGraficos=this;
        this.layoutPrincipal=dijit.byId("principal");

//        this.grillaCompare=dijit.byId("grillaCompare");
 //       this.grillaTarget=dijit.byId("grillaTarget");

},
test:function(nodo)
{
	var chart1 = new dojox.charting.Chart2D(nodo);
chart1.addPlot("default", {type: "Bars"});
chart1.addPlot("other", {type: "Areas"});
chart1.addAxis("x",{
	labels:[
{value:1,text:"hola"},
{value:2,text:"chau"},
{value:3,text:"asdf"},
{value:4,text:"ffff"},
{value:5,text:"asdfd"},
{value:6,text:"fdf"},
{value:6,text:"dfdf"},{value:7,text:"dfdf"}
]
});
chart1.addAxis("y", {vertical: true});
chart1.addSeries("Series 1", [1, 2, 2, 3, 4, 5, 5, 7]);
chart1.addSeries("Series 2", [1, 1, 4, 2, 1, 6, 4, 3],
    {plot: "other", stroke: {color:"blue"}, fill: "lightblue"});
chart1.render();
	
	
	
},
smooth:function(node)
{
	
	new dojox.charting.Chart(node)
		.addPlot("default", { type: "Areas", tension: "X" })
		.setTheme(dojox.charting.themes.Shrooms)
		.addSeries("Series A", [1, 2, 0.5, 1.5, 1, 2.8, 0.4])
		.addSeries("Series B", [2.6, 1.8, 2, 1, 1.4, 0.7, 2])
		.addSeries("Series C", [6.3, 1.8, 3, 0.5, 4.4, 2.7, 2])
		.render();
	
	
},
otro:function(node)
{
	
//	The form of data in a data series can take a number of forms: a simple array,
//an array of objects {x,y}, or something custom (as determined by the plot).
//Here's an example of a Candlestick chart, which expects an object of
//{ open, high, low, close }.
	new dojox.charting.Chart(node)
		.addPlot("default", {type: "Candlesticks", gap: 1})
		.addAxis("x", {fixLower: "major", fixUpper: "major", includeZero: true})
		.addAxis("y", {vertical: true, fixLower: "major", fixUpper: "major", natural: true})
		.addSeries("Series A", [
				{ open: 20, close: 16, high: 22, low: 8 },
				{ open: 16, close: 22, high: 26, low: 6, mid: 18 },
				{ open: 22, close: 18, high: 22, low: 11, mid: 21 },
				{ open: 18, close: 29, high: 32, low: 14, mid: 27 },
				{ open: 29, close: 24, high: 29, low: 13, mid: 27 },
				{ open: 24, close: 8, high: 24, low: 5 },
				{ open: 8, close: 16, high: 22, low: 2 },
				{ open: 16, close: 12, high: 19, low: 7 },
				{ open: 12, close: 20, high: 22, low: 8 },
				{ open: 20, close: 16, high: 22, low: 8 },
				{ open: 16, close: 22, high: 26, low: 6, mid: 18 },
				{ open: 22, close: 18, high: 22, low: 11, mid: 21 },
				{ open: 18, close: 29, high: 32, low: 14, mid: 27 },
				{ open: 29, close: 24, high: 29, low: 13, mid: 27 },
				{ open: 24, close: 8, high: 24, low: 5 },
				{ open: 8, close: 16, high: 22, low: 2 },
				{ open: 16, close: 12, high: 19, low: 7 },
				{ open: 12, close: 20, high: 22, low: 8 },
				{ open: 20, close: 16, high: 22, low: 8 },
				{ open: 16, close: 22, high: 26, low: 6 },
				{ open: 22, close: 18, high: 22, low: 11 },
				{ open: 18, close: 29, high: 32, low: 14 },
				{ open: 29, close: 24, high: 29, low: 13 },
				{ open: 24, close: 8, high: 24, low: 5 },
				{ open: 8, close: 16, high: 22, low: 2 },
				{ open: 16, close: 12, high: 19, low: 7 },
				{ open: 12, close: 20, high: 22, low: 8 },
				{ open: 20, close: 16, high: 22, low: 8 }
			],
			{ stroke: { color: "green" }, fill: "lightgreen" }
		)
		.render();
	
	
	
	
	
	
}
});
