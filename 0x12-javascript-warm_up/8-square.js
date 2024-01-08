#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

const size = parseInt(args[0], 10);

if (!isNaN(size)) {
for (let i = 0; i < size; i++) {
let line = "";
for (let j = 0; j < size; j++) {
line += 'X';
}
console.log(line);
}
} else {
console.log("Missing size");
}

