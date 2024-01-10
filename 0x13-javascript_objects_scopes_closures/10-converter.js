#!/usr/bin/node

export.converter = function(base) {
	return function (number) {
		return number.tostring(base);
	};
};
