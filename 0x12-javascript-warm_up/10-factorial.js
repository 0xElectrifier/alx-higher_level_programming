#!/usr/bin/node
let num = process.argv[2];
if (isNaN(num)) {
    num = 1;
}
function factorial (num) {
  if (num < 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(num));
