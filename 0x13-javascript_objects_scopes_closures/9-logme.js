#!/usr/bin/node

let argprinted = 0;

exports.logMe = function (item) {
	console.log(`${argprinted}: ${item}`);
	argprinted;
};
