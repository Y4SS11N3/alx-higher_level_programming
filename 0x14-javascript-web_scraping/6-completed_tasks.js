#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});
