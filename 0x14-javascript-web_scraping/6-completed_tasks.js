#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.completed);
    const completedTasksByUser = completedTasks.reduce((acc, task) => {
      acc[task.userId] = (acc[task.userId] || 0) + 1;
      return acc;
    }, {});
    console.log(completedTasksByUser);
  }
});
