#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    const filmsData = JSON.parse(body);
    // Filter films where Wedge Antilles is present (character ID 18)
    const moviesWithWedgeAntilles = filmsData.results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(moviesWithWedgeAntilles.length);
  }
});
