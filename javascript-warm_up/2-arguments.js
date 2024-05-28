#!/usr/bin/node
const numArgs = process.argv.length - 2;
if (numArgs === 0) {
  console.log('no argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments');
}
