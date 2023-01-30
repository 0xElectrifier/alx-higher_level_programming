#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const width = this.width;
    const height = this.height;
    if (width && height) {
      for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  }

  rotate () {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
