#!/usr/bin/node
const dictIn = require('./101-data.js').dict;
const dictOut = {};

for (const userId in dictIn) {
  const occur = dictIn[userId];
  // Avoid iterating an occurence repeatedly
  // if (dictOut.hasOwnProperty(occur)) continue;
  if (!Object.prototype.hasOwnProperty.call(dictOut, occur)) {
    dictOut[occur] = [];
  }
  dictOut[occur].push(userId);
}
console.log(dictOut);
