#!/usr/bin/node
const argument = process.argv[2];
const parsedInt = parseInt(argument);
console.log(isNaN(parsedInt) ? 'Not a number' : 'My number: ' + parsedInt);
