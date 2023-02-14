#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) c = 'X';

    width = self.width;
    height = self.height;
    if (width && height) {
      for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  }
};
