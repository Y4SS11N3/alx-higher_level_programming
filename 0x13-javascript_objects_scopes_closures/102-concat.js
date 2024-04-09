#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, { encoding: 'utf8', flag: 'r' });
const contentB = fs.readFileSync(fileB, { encoding: 'utf8', flag: 'r' });

fs.writeFileSync(fileC, contentA + contentB);
