#!/usr/bin/node
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const parsedInt = parseInt(arg);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
