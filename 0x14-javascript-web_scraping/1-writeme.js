#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const file = argv[2];
const content = argv[3];
// Quit script if third argument wasn't passed
if (content === undefined) process.exit();

fs.writeFile(file, content, error => {
  if (error) console.log(error);
});
