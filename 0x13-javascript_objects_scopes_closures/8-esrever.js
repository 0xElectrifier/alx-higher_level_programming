#!/usr/bin/node
exports.esrever = function (list) {
  if (!Array.isArray(list)) return;

  let temp;
  const listLen = list.length;
  let firstHalf = 0;
  let secondHalf = listLen - 1;

  while (firstHalf < Math.floor(listLen / 2)) {
    temp = list[firstHalf];
    list[firstHalf] = list[secondHalf];
    list[secondHalf] = temp;

    firstHalf++;
    secondHalf--;
  }
  return (list);
};
