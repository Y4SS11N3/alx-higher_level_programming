#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characterUrls = JSON.parse(body).characters;

  const characterPromises = characterUrls.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then((characters) => {
      characters.forEach((character) => {
        console.log(character);
      });
    })
    .catch((err) => {
      console.error(err);
    });
});
