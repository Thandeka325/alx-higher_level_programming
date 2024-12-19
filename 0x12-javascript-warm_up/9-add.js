#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstArg = parseInt(process.argv[2], 10);
const secondArg = parseInt(process.argv[3], 10);

if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  console.log(add(firstArg, secondArg));
}
