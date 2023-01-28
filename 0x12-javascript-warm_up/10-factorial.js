#!/usr/bin/node
let arg = process.argv[2];
arg = parseInt(arg);

function factorial (a) {
  if (isNaN(a) || a === 0) return (1);
  return (a * factorial(a - 1));
}
console.log(factorial(arg));
