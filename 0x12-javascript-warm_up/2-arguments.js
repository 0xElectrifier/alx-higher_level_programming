#!/usr/bin/node
const argv = require('process').argv;
const argLen = argv.length;

if (argv[2] === undefined) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
