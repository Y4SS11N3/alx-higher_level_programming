#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      film.characters.forEach((characterUrl) => {
        if (characterUrl.endsWith('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
