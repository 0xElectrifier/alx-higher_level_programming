#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
if (!file) process.exit(); // Exit script if no argument was passed

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
