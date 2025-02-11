#!/usr/bin/node
// Script that prints the number of movies where Wedge Antilles (ID 18) is present

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const movies = data.results.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(movies.length);
  }
});
