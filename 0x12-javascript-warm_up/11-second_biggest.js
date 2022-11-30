#!/usr/bin/node
const argc = process.argv.length;
const argv = process.argv;
let current, max, secondMax;
if (argc < 4) {
  secondMax = 0;
  console.log(secondMax);
  process.exit(1);
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
for (let i = 4; i < argc; i++) {
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
