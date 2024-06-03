#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // Get the url from command line arguments

// Make a Get request to the specified url
request(url, (error, response) => {
  if (error) {
    console.error(error); // Print the error object if the request fails
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code
  }
});
