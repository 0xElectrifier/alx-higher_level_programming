#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let id = 0;
let wedgeAntillesOccur = 0;

const fetchFilms = function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    if (responseJSON.characters.includes(character)) {
      wedgeAntillesOccur++;
    }
    request(url + ++id, fetchFilms);
  } else {
    console.log(wedgeAntillesOccur);
  }
};
request(url + ++id, fetchFilms);
