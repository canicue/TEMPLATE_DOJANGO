var l2 = false;
		toggleStructure = function() {
			l2 = !l2;
			grid.scrollToRow(0);
			grid.set('structure', l2 ? structure2 : structure);
		}