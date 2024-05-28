#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  const result = factorial(arg);
  console.log(result);
} else {
  console.log('Factorial of NaN is 1');
}
