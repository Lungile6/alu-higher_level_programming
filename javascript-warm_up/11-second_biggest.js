#!/usr/bin/node
function findSecondLargest (arr) {
  if (arr.length < 2) {
    return 0;
  }

  // Sort the array in ascending order
  arr.sort((a, b) => a - b);

  // The second largest element is at index arr.length - 2
  return arr[arr.length - 2];
}

const args = process.argv.slice(2).map(Number);
const secondLargest = findSecondLargest(args);

console.log(secondLargest);
