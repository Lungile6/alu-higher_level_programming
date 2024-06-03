#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2]; // Get the file path from command line arguments
const contentToWrite = process.argv[3]; // Get the sstring to write from command line arguments

// Write the content to the file asynchronously
fs.writeFile(filepath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if writing fails
  } else {
    console.log(`Content written to ${filepath}`);
  }
});
