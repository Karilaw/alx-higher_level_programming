#!/usr/bin/node
const request = require('request');

function getCharacterName (url, i, characters) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        getCharacterName(characters[i + 1], i + 1, characters);
      }
    }
  });
}

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    getCharacterName(characters[0], 0, characters);
  }
});
