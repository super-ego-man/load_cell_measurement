Hello!

This code and circuit design take measurements for the
strain-controlled cyclic fatigue test created at Tennessee Tech
University by Marsalis Pullen, Haley Finegan, and Oliver Kisielius,
under the mentorship of Dr. Stretz, as part of a Research Experience
for Undergraduates program sponsored by the NSF. The code is in
Python.

To run this code, you need Oliver's version of
Adafruit_Python_ADS1x15, found at
https://github.com/super-ego-man/Adafruit_Python_ADS1x15
This and other requirements can be found in the documentation.

Some of the instructions in the docs subdirectory are aimed at people
who have never used a Raspberry Pi before. Maybe I flatter myself by
imagining anybody will continue the project that my team started this
summer. We were pretty close to getting nice results.

You also need RPi.GPIO and Adafruit_Python_GPIO, although the latter
is just a wrapper for the former. (Hopefully it wouldn't be terrible
to convert this (or any other) code to use a USB I2C adapter instead
of a 'Pi, with a wrapper like that. If you do this, please consider
letting me know, because I'll be flattered.)

Right now this code is not in a useable state. That is, if you follow the
directions in this repository, it won't work, and stuff won't be documented.
I intend to fix this pretty soon, although I won't be able to push my updates
next week. See the TODO list.
