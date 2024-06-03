#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2]; // Get the URL from command line arguments
const filePath = process.argv[3]; // Get the file path to store

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if the request fails
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err); // Print the error object if writing fails
      } else {
        console.log(`Content written to ${filePath}`);
      }
    });
  }
});
