#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const movieURL = 'https://swapi-api.alx-tools.com/api/films/' + movieID;
function fetchName (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
      process.exit();
    }
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }
  });
}

request(movieURL, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const charIndex in characters) {
      fetchName(characters[charIndex]);
    }
  }
});
