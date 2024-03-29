#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
if (id === undefined) process.exit();

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  } else {
    console.log(error);
  }
});
