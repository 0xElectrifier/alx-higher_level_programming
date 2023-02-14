#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) c = 'X';

    const width = this.width;
    const height = this.height;
    if (width && height) {
      for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
