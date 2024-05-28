#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (!isNaN(size) && size > 0) {
  for (let row = 0; row < size; row++) {
    let line = '';
    for (let col = 0; col < size; col++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
