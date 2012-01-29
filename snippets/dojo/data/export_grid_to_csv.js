var items_to_csv = function(items){
			var csvResults = dojo.byId('csvResults');
			var first_row = [];
			dojo.forEach(grid.layout.cells, function(cell){
				first_row.push(cell.name);
			});
			csvResults.value = first_row.join(',') + "\n";
			dojo.forEach(items, function(item, i){
				var result = [];
				dojo.forEach(grid.layout.cells, function(cell){
					result.push(cell.format(i, item));
				});
				csvResults.value += result.join(',') + "\n";
			});
		}
		var export_all = function(){
			var store = grid.store;
			store.fetch({
				query: grid.query,
				sort: grid.getSortProps(),
				queryOptions: grid.queryOptions,
				onComplete: function(items){
					items_to_csv(items);
				}
			});
		}
		var export_selected = function(){
			items_to_csv(grid.selection.getSelected());
		}