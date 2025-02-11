#!/usr/bin/node
// Script that prints the number of movies where Wedge Antilles (ID 18) is present

const request = require('request');
let num = 0;

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
	if (character.includes(18)) {
	 num += 1;
	}
	});
       });
    console.log(num);
  }
});
