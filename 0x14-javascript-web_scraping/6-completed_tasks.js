#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const tasksCompleted = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (tasksCompleted[tasks[i].userId]) {
          tasksCompleted[tasks[i].userId]++;
        } else {
          tasksCompleted[tasks[i].userId] = 1;
        }
      }
    }
    console.log(tasksCompleted);
  }
});
