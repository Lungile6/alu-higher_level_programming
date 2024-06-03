#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from command line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a get a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error onject if the request fails
  } else {
    const movieData = JSON.parse(body);

    console.log(movieData.title); // Print the movie title
  }
});
