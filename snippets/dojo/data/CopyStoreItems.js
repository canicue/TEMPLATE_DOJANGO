var origStore = some.datastore();
var newStore = null;

function onComplete(items, request) {
  newStore = some.datastore();
  if (items && items.length > 0) {
    var i;
    for (i = 0; i < items.length; i++) {
      var item = items[i];
      var attributes = origStore.getAttributes(item);
      if (attributes && attributes.length > 0) {
        var j;
        for (j = 0; j < attributes.length; j++) {
          var newItem = {};
          var values = origStore.getValues(item, attributes[j]);

          //Be careful here. If you reference other items then those too have to be cloned over in a similar manner (iterating over the attributes and building up a structure for a newItem call. This pseudocode doesn't really take that into accoumt.
          if (values) {
            if (values.length > 1) {
              //Create a copy.
              newItem[attributes[j]] = values.slice(0, values.length);
            } else {
              newItem[attributes[j]] = values[0];
            }
        }
      }
      newStore.newItem(newItem);
    }
  }
}}
origStore.fetch({query:{} , onComplete: onComplete});