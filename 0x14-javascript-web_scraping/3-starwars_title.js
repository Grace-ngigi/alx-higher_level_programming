#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    const movieData = JSON.parse(body);
    if (movieData.title) {
      console.log(movieData.title);
    } else {
      console.log('Movie not found for the given ID.');
    }
  }
});
