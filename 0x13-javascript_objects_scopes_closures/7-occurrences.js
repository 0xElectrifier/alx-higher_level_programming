#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (!Array.isArray(list)) return;

  const listLen = list.length;
  let count = 0;
  for (let i = 0; i < listLen; i++) {
    if (list[i] === searchElement) count++;
  }
  return (count);
};
