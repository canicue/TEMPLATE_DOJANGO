var store = new dojo.data.ItemFileReadStore({data: { identifier: "uniqueId",
  items: [ {uniqueId: 1, status:"CLOSED"},
    {uniqueId: 2,  status:"OPEN"},
        {uniqueId: 3,  status:"PENDING"},
        {uniqueId: 4,  status:"BLOCKED"},
        {uniqueId: 5,  status:"CLOSED"},
        {uniqueId: 6,  status:"OPEN"},
        {uniqueId: 7,  status:"PENDING"},
        {uniqueId: 8,  status:"PENDING"},
        {uniqueId: 10, status:"BLOCKED"},
        {uniqueId: 12, status:"BLOCKED"},
        {uniqueId: 11, status:"OPEN"},
        {uniqueId: 9,  status:"CLOSED"}
      ]
}});

//Define the comparator function for status.
store.comparatorMap = {};
store.comparatorMap["status"] = function(a,b) {
  var ret = 0;
  // We want to map these by what the priority of these items are, not by alphabetical.
  // So, custom comparator.
  var enumMap = { OPEN: 3, BLOCKED: 2, PENDING: 1, CLOSED: 0};
  if (enumMap[a] > enumMap[b]) {
    ret = 1;
  }
  if (enumMap[a] < enumMap[b]) {
    ret = -1;
  }
  return ret;
};

var sortAttributes = [{attribute: "status", descending: true}, { attribute: "uniqueId", descending: true}];
function completed(items, findResult){
  for(var i = 0; i < items.length; i++){
    var value = store.getValue(items[i], "uniqueId");
    console.log("Item ID: [" + store.getValue(items[i], "uniqueId") + "] with status: [" + store.getValue(items[i], "status") + "]");
  }
}
function error(errData, request){
  console.log("Failed in sorting data.");
}

//Invoke the fetch.
store.fetch({onComplete: completed, onError: error, sort: sortAttributes});