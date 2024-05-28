#!/usr/bin/node
// check if any arguments were passed
if (console.argv2 !== undefined) {
  // Print the first argument
  console.log(process.argv2);
} else {
  // No argument provided
  console.log('No argument');
}
