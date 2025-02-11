#!/usr/bin/node
// Script that computes the number of tasks completed by user ID

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
