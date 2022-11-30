#!/usr/bin/node
let num = process.argv[2];
if (isNaN(num)) {
  console.log('Not a number');
  process.exit(1);
}
num = parseInt(num);
console.log(`My number: ${num}`);
