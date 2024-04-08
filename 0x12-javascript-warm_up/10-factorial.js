#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const n = parseInt(process.argv[2], 10);
console.log(factorial(n));
