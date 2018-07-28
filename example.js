var LedMatrix = require(".");

var matrix = new LedMatrix(16, 2, 1);
matrix.fill(255, 0, 0);

console.log("reported width: " + matrix.getWidth() );
console.log("reported height: " + matrix.getHeight() );

setTimeout(function () {
	matrix.clear();
}, 1500);
