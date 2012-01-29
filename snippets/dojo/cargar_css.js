 mylib: {
    addStyle: function(/*String*/modulePath) {
      //summary: loads a CSS file based on a modulePath.
      var url = dojo.moduleUrl(modulePath).toString();
      //Adjust URL a bit so we get dojo.require-like behavior
      url = url.substring(0, url.length - 1) + ".css";
      var link = dojo.create("link", {
        type: "text/css",
        rel: "stylesheet",
        "data-mylibstylename": modulePath,
        href: url
      });
      dojo.doc.getElementsByTagName("head")[0].appendChild(link);
    },

    removeStyle: function(/*String*/modulePath) {
      //summary: removes the link tag that was associated with the modulePath.
      dojo.query('[data-mylibstylename="' + modulePath + '"]').orphan();
    }
 }
