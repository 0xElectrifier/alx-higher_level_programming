#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  }
  const tasksOccur = {};
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    for (const taskIndex in todos) {
      const currentTodo = todos[taskIndex];
      const userId = currentTodo.userId;
      // Skip uncompleted tasks
      if (currentTodo.completed === false) continue;

      // if (!Object.prototype.hasOwnProperty(tasksOccur, userId)) {
      if (!(userId in tasksOccur)) {
        tasksOccur[userId] = 1;
      } else {
        tasksOccur[userId] += 1;
      }
    }
  }
  console.log(tasksOccur);
});
