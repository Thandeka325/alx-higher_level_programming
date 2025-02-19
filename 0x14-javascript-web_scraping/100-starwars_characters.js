#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.log(charErr);
      } else {
        console.log(JSON.parse(charBody).name);
      }
    });
  });
});
