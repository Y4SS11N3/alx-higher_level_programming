#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, async (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
