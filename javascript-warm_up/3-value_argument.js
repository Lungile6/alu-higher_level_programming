#!/usr/bin/node
// Check if any arguments were passed
if (process.argv[2] !== undefined) {
  // Print the first argument
  console.log(process.argv[2]);
} else {
  // No argument provided
  console.log('No argument');
}
