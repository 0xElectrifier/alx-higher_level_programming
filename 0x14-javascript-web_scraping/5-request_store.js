#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const outputFile = argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }
  if (response.statusCode === 200) {
    fs.writeFile(outputFile, body, err => err ? console.log(err) : {});
  }
});
