function itemToJSON(store, item) {
  // summary: Function to convert an item into a JSON format.
  // store:
  //    The datastore the item came from.
  // item:
  //    The item in question.
  var json = {};
  if (item && store) {
    //Determine the attributes we need to process.
    var attributes = store.getAttributes(item);
    if (attributes && attributes.length > 0) {
      var i;
      for (i = 0; i < attributes.length; i++) {
        var values = store.getValues(item, attributes[i]);
        if (values) {
          //Handle multivalued and single-valued attributes.
          if (values.length > 1 ) {
            var j;
            json[attributes[i]] = [];
            for (j = 0; j < values.length; j++ ) {
              var value = values[j];
              //Check that the value isn't another item. If it is, process it as an item.
              if (store.isItem(value)) {
                json[attributes[i]].push(dojo.fromJson(itemToJSON(store, value)));
              } else {
                json[attributes[i]].push(value);
              }
            }
          } else {
            if (store.isItem(values[0])) {
               json[attributes[i]] = dojo.fromJson(itemToJSON(store, values[0]));
            } else {
               json[attributes[i]] = values[0];
            }
          }
        }
      }
    }
  }
  return dojo.toJson(json);
}