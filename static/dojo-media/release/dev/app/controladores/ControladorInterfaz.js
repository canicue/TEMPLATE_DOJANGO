dojo.provide("desktop.controladores.ControladorInterfaz");
dojo.require("dijit.dijit");
dojo.require("dijit.Dialog");
dojo.require("dojo.io.iframe");
dojo.require("dojox.layout.FloatingPane");
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dijit.layout.TabContainer");
dojo.require("dijit.layout.AccordionContainer");
dojo.require("dijit.form.Button");

dojo.declare("desktp.controladores.ControladorInterfaz",[],{
_principal:null,
_central:null,
 
    constructor:function()
    {
    	dojo.global.controladorInterfaz=this;
        this._principal=new dijit.layout.BorderContainer(
        {
        	style:{height:"100%;width:100%"}	
        	
        	
        }
        
        );
        
       this._central=new dijit.layout.ContentPane(); 
        this._principal.addChild(this._central);
        document.body.appendChild(this._principal.domNode);
        
        
        this.layoutPrincipal=dijit.byId("principal");



}
});
