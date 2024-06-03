#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2]; // Get the API URL from command line arguments
const characterId = 18; // Character ID for Wedge Antilles

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if the request fails
  } else {
    const filmsData = JSON.parse(body);
    const filmsWithWedge = filmsData.results.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(filmsWithWedge.length); // Print the number of movies
  }
});
