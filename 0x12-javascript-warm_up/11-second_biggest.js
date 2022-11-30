#!/usr/bin/node
const argc = process.argv.length - 2;
const argv = process.argv;
let current, max, secondMax;
if (argc == 0 || argc == 1) {
  secondMax = 0;
} 
 
if (argv[3] > argv[2]) {
  max = argv[3];
  secondMax = argv[2];
} else {
  max = argv[2];
  secondMax = argv[3];
}
max = parseInt(max);
secondMax = parseInt(secondMax);
for (let i = 4; i < (argc + 2); i++) {
  current = parseInt(argv[i]);
  if (current > max) {
    if (secondMax < max) {
      secondMax = max;
      max = current;
    }
  } else if (current < max) {
    if (current > secondMax) {
      secondMax = current;
    }
  }
}

console.log(secondMax);
