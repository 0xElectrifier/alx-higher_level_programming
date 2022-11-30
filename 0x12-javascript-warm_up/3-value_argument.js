#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
  process.exit(1);
}
console.log(argv[2]);
