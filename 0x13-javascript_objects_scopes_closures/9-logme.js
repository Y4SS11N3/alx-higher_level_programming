#!/usr/bin/node
let printCount = 0;

exports.logMe = function (item) {
  console.log(`${printCount}: ${item}`);
  printCount++;
};
