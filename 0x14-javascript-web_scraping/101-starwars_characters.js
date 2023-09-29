#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    function fetchCharacter (index) {
      if (index < characterUrls.length) {
        request.get(characterUrls[index], (err, res, characterBody) => {
          if (err) {
            console.error('Error occurred while fetching character data:', err);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            fetchCharacter(index + 1);
          }
        });
      }
    }

    fetchCharacter(0);
  }
});
