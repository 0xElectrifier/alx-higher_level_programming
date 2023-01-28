#!/usr/bin/node
const arg = require('process').argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(`${arg}`);
}
