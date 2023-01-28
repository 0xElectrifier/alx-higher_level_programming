#!/usr/bin/node

function searchSecLargest (arr) {
  let largest = argv[2];
  let sLargest = argv[2];
  const argLen = argv.length;
  if (argLen < 4) sLargest = 0;

  for (let i = 2; i < argLen; i++) {
    if (argv[i] > largest) {
      sLargest = largest;
      largest = argv[i];
    } else if (argv[i] > sLargest && argv[i] !== largest) {
      sLargest = argv[i];
    }
  }
  return (sLargest);
}
const argv = process.argv;
console.log(searchSecLargest(argv));
