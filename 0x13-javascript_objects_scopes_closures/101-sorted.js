#!/usr/bin/node
const dictIn = require('./101-data.js').dict;
const dictOut = {};

for (let userId in dictIn) {
  const occur = dictIn[userId];
  // Avoid iterating an occurence repeatedly
  // if (dictOut.hasOwnProperty(occur)) continue;
  if (!dictOut.hasOwnProperty(occur)) {
    dictOut[occur] = [];
  }
  dictOut[occur].push(userId);
}
console.log(dictOut);
