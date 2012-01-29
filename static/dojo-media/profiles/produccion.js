dependencies ={
	//	releaseDir:'../../../../static/dojo-media/release/',
		action:'release',
		releaseDir:'../../../../../../static/dojo-media/release/',
		releaseName:'prod' ,
		internStrings:true,
		cssOptimize:"comments",
		stripConsole:"all",
		optimize:"shrinksafe",
		layerOptimize:"shrinksafe",
	//	profileFile:"../../../../static/dojo-media/release/profiles/perfil.js"
		
    layers:  [
        {
            name: "../layers/login_layer.js",
            dependencies: [

                // From testBuildSystemFoo.html
           //       "dojo.parser",
                    "dojox.widget.Standby",
        "dijit.form.Button",
]
        },

          {
            name: "../layers/menu_layer.js",
            dependencies: [

          "dijit.MenuBar",
        "dijit.PopupMenuBarItem"

    ]
    },

              {
            name: "../layers/layout_layer.js",
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
            name: "../layers/index_layer.js",
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
            name: "../layers/mentions_layer.js",
            dependencies: [

"mentions.ControladorNuevo",
"mentions.interfaz",
"mentions.widgets.Info",
"mentions.widgets.Prueba",
"mentions.widgets.Paginador",
"mentions.widgets.Botoncito",
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
            name: "../layers/desktop_layer.js",
            dependencies: [
//"desktop.BuscadorGoogle",
"desktop.ControladorAplicacion",
"desktop.controladores.ControladorStores",
//"desktop.Datos",
//"desktop.Formatter",
//"desktop.widget.Busqueda",
//"desktop.widget.Objetivo",
//"desktop.widget.SliderBusquedas",
"dijit.Tooltip",
"dijit.Tooltipdialog",
"dijit.form.CheckBox",
"dijit.form.ComboBox",
"dijit.form.DateTextBox",
"dijit.form.DropDownButton",
"dijit.form.Form",
"dijit.form.Select",
"dijit.form.Textarea",
"dijit.layout.AccordionContainer",
"dijit.layout.BorderContainer",
"dijit.layout.ContentPane",
"dijit.layout.TabContainer",
"dojo.NodeList-manipulate",
"dojo.NodeList-traverse",
"dojo.data.ItemFileReadStore",
"dojo.data.ItemFileWriteStore",
"dojo.dnd.Source",
"dojo.fx.easing",
"dojo.io.script",
"dojox.data.GoogleSearchStore",
"dojox.grid.DataGrid",
"dojox.grid.EnhancedGrid",
"dojox.grid.enhanced.plugins.Pagination",
"dojox.grid.enhanced.plugins.exporter.CSVWriter",
"dojox.grid.cells.dijit",
"dojox.layout.ExpandoPane",
"dojox.layout.FloatingPane",
"dojox.layout.GridContainer",
"dojox.mdnd.AreaManager",
"dojox.mdnd.DropIndicator",
"dojox.mdnd.dropMode.VerticalDropMode",
//"dojox.rpc.Service",
"dojox.widget.FeedPortlet",
//"mentions.data.FriendfeedStore",
//"mentions.data.YahooStore",
//"mentions.widgets.TopSites",
"mentions.widgets.TopUsers",
"desktop.controladores.ControladorStores",
"desktop.controladores.ControladorCompare",
	 "dojox.form.ListInput"




    ]
    }





    ],
    prefixes: [
        [ "dijit", "../dijit" ],
        [ "dojox", "../dojox"],
        [ "mentions", "../mentions"],
        [ "desktop", "../desktop"],
        ["layers","../layers"]/* atenti con esta cabronada!!!!*/
    ]
};
