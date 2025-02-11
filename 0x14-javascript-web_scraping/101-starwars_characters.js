#!/usr/bin/node
// Script that prints all characters of a Star Wars movie in the order from API

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
