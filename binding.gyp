{
	"targets": [
		{
	        "target_name": "node-rpi-rgb-led-matrix",
	        "sources": [ "src/base.cc", "src/ledmatrix.cc", "src/image.cc" ],
	        "dependencies": [ "./binding.gyp:rpi-rgb-led-matrix" ],
	        "include_dirs": [ "./external/matrix/include", "./include/", "<!(nodejs -e \"require('nan')\")" ]
	    },
		{
			"target_name": "rpi-rgb-led-matrix",
			"type": "static_library",
			"sources":
				["external/matrix/lib/bdf-font.cc",
				"external/matrix/lib/content-streamer.cc",
				"external/matrix/lib/framebuffer.cc",
				"external/matrix/lib/gpio.cc",
				"external/matrix/lib/graphics.cc",
				"external/matrix/lib/hardware-mapping.c",
				"external/matrix/lib/led-matrix.cc",
				"external/matrix/lib/led-matrix-c.cc",
				"external/matrix/lib/multiplex-transformers.cc",
				"external/matrix/lib/options-initialize.cc",
				"external/matrix/lib/thread.cc",
				"external/matrix/lib/transformer.cc"],
			"libraries": ["-lrt", "-lm", "-lpthread"],
			"defines": ['DEFAULT_HARDWARE="adafruit-hat"'],
			"include_dirs": [ "external/matrix/include" ],
	        "direct_dependent_settings": {
	            "include_dirs": [ "external/matrix/include" ]
	        }
		}
	]
}
