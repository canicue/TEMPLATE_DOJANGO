dependencies ={
	//	releaseDir:'../../../../static/dojo-media/release/',
		action:'release',
	//	releaseDir:'../../../static/dojo-media/release/',
		releaseName:'devorrar' ,//buscar la imagen del menu!!!!!!!!!!!!!!
		internStrings:false,
		//cssOptimize:"comments",
	//	stripConsole:"all",
	//	optimize:"shrinksafe",
	//	layerOptimize:"shrinksafe",
	//	profileFile:"../../../../static/dojo-media/release/profiles/perfil.js"
		
    layers:  [
        {
            name: "../../../layers/login_layer.js",
            dependencies: [

                // From testBuildSystemFoo.html
           //       "dojo.parser",
                    "dojox.widget.Standby",
        "dijit.form.Button",
]
        },

          {
            name: "../../../layers/menu_layer.js",
            dependencies: [

          "dijit.MenuBar",
        "dijit.PopupMenuBarItem"

    ]
    },

              {
            name: "../../../layers/layout_layer.js",
            dependencies: [


        "dijit.layout.BorderContainer",
        "dijit.layout.TabContainer",
        "dijit.layout.AccordionContainer",
        "dijit.layout.ContentPane",
        "dojox.widget.Portlet",
        "dojox.layout.GridContainer",
        "dojox.layout.TableContainer",
        "dojox.layout.ResizeHandle"


    ]
    },
      {
            name: "../../../layers/index_layer.js",
            dependencies: [


        "dijit.layout.TabContainer",
        "dijit.layout.AccordionContainer",
        "dijit.layout.ContentPane",
        "dojox.widget.Portlet",
        "dojox.layout.GridContainer",
        "dojox.layout.TableContainer",



    ]
    },
         {
            name: "../../../layers/mentions_layer.js",
            dependencies: [


"dojox.widget.Standby",
"dijit.form.DropDownButton",
"dijit.TitlePane",
"dijit.form.Button",
"dojox.widget.AutoRotator",
"dijit.TitlePane",
"dijit.form.CheckBox",
"dojox.form.BusyButton",
"dijit.form.MultiSelect",
"dijit.InlineEditBox",
"dijit.MenuBar",
"dijit.PopupMenuBarItem",
"dijit.form.ComboBox",
"dijit.form.Form",
"dijit.form.Textarea",
"dijit.form.Select",
"dijit.Dialog",
"dijit.ColorPalette",
"dijit.ProgressBar",
"mentions.widgets.TimeFilter",

"dijit.form.DateTextBox"



    ]
    },
          {
            name: "../../../layers/desktop_layer.js",
            dependencies: [
            

 		"dojo.NodeList-manipulate",



"dojox.mdnd.AreaManager",
"dojox.mdnd.DropIndicator",
"dojox.mdnd.dropMode.VerticalDropMode",
"dojox.grid.DataGrid",
"dojo.dnd.Source",
"dojox.widget.FeedPortlet",

"dojox.layout.ExpandoPane",
"dojo.data.ItemFileReadStore",
"dijit.form.ComboBox",
"dojo.NodeList-traverse",
"dijit.layout.AccordionContainer",
"dijit.layout.TabContainer",
"dijit.layout.ContentPane",
"dijit.layout.BorderContainer",
"dojox.layout.FloatingPane",
"dojo.fx.easing",
 "dojox.form.ListInput",
"dojo.io.script",
"dojox.layout.GridContainer",
"dijit.Tooltip",
	
 		"dojo.NodeList-manipulate",


		"dojo.data.ItemFileWriteStore",		       

		
		

		"dijit.form.Form",
		"dijit.form.DateTextBox",
		"dijit.form.DropDownButton",
		"dijit.TooltipDialog",
		"dijit.form.CheckBox",
		"dijit.form.Select",
		"dijit.form.Textarea"
		




//"desktop.ControladorAplicacion"




    ]
    }





    ],
    prefixes: [
        [ "dijit", "../dijit" ],
        [ "dojox", "../dojox"],
        [ "mentions", "../mentions"],
        [ "desktop", "../desktop"],
       ["layers","../../../layers"]/* atenti con esta cabronada!!!!(tira el moco de nls si no esta!!!*/
    ]
};
