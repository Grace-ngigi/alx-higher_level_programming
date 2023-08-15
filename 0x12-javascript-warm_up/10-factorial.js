#!/usr/bin/node
function factorial (n) {
  return isNaN(n) ? 1 : (n === 0 ? 1 : n * factorial(n - 1));
}

const argument = process.argv[2];
const num = parseInt(argument);

const result = factorial(num);
console.log(result);
