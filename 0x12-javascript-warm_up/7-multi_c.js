#!/usr/bin/node
const count = process.argv[2];
if (isNaN(count)) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < count; i++) {
  console.log('C is fun');
}
