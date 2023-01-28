#!/usr/bin/node

function searchSecLargest (arr) {
  let largest = argv[2];
  let sLargest = argv[2];
  let current;
  const argLen = argv.length;
  if (argLen < 4) sLargest = 0;

  // Find the FIRST second largest integer
  for (let i = 2; i < argLen; i++) {
    if (argv[i] < sLargest) {
      sLargest = argv[i];
      break;
    }
  }

  for (let i = 2; i < argLen; i++) {
    current = argv[i];
    if (current > largest) {
      sLargest = largest;
      largest = current;
    } else if (current > sLargest && current !== largest) {
      sLargest = current;
    }
  }
  return (sLargest);
}
const argv = process.argv;
console.log(searchSecLargest(argv));
