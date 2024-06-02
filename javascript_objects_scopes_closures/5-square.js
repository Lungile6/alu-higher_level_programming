#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // Initialize instance attributes if w and h are positive integers
      this.width = w;
      this.height = h;
    } else {
      // Throw an error if w or h is not a positive integer
      throw new Error('Width and height must be positive integers');
    }
  }
}

module.exports = Rectangle;
