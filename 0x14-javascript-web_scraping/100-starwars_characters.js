#!/usr/bin/node
const request = require('request');

function getCharacterName (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      getCharacterName(characters[i]);
    }
  }
});
