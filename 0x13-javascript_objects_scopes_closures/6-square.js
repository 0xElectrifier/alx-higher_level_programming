#!/usr/bin/node
const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  constructor (size) {
    super(size);
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
