#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};
console.log(myObject);

myObject.incr();
console.log(myObject); // value: 13

myObject.incr();
console.log(myObject); // value: 14

myObject.incr();
console.log(myObject); // value: 15
