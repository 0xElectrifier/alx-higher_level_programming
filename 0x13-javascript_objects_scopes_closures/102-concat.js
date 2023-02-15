#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const firstFile = argv[2];
const secondFile = argv[3];
const outputFile = argv[4];

try {
  fs.readFile(firstFile, 'utf8', (err1, firstData) => {
    fs.readFile(secondFile, 'utf8', (err2, secondData) => {
      fs.writeFile(outputFile, firstData + secondData, () => {});
    });
  });
} catch {}
