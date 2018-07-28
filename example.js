var LedMatrix = require("./node-rpi-rgb-led-matrix");

var matrix = new LedMatrix(16, 2, 1);
matrix.fill(255, 50, 100);
matrix.setPixel(0, 0, 0, 50, 255);
