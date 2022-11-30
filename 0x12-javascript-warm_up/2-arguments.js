#!/usr/bin/node
const args = process.argv.length - 2;
if (args === 0) {
  console.log('No argument');
  process.exit(1);
} else if (args === 1) {
  console.log('Arguments found');
  process.exit(0);
} else {
  console.log('Arguments found');
}
