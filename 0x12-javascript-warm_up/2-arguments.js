#!/usr/bin/node
const args = process.argv.length;
console.log(args < 3 ? 'No argument' : args === 3 ? 'Argument found' : 'Arguments found');
