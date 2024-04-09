#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  list.forEach(item => reversed.unshift(item));
  return reversed;
};
