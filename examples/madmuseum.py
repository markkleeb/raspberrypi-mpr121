# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121

# Thanks to Scott Garner & BeetBox!
# https://github.com/scottgarner/BeetBox/

print 'Adafruit MPR121 Capacitive Touch Audio Player Test'

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
#cap.begin(address=0x5B)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(busnum=1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

cap.set_thresholds(10, 4)

# Define mapping of capacitive touch pin presses to sound files
# tons more sounds are available but because they have changed to .flac in /opt/sonic-pi/etc/samples/ some will not work
# more .wav files are found in /usr/share/scratch/Media/Sounds/ that work fine this example uses Aniamal sounds.

#SOUND_MAPPING = {
#0: '/opt/sonic-pi/etc/samples/ambi_piano.flac',
  #1: '/opt/sonic-pi/etc/samples/elec_hollow_kick.flac',
  #2: '/opt/sonic-pi/etc/samples/ambi_soft_buzz.flac',
  #3: '/opt/sonic-pi/etc/samples/bass_dnb_f.flac',
  #4: '/opt/sonic-pi/etc/samples/bass_hit_c.flac',
  #5: '/opt/sonic-pi/etc/samples/elec_plip.flac',
  #6: '/opt/sonic-pi/etc/samples/bass_trance_c.flac',
  #7: '/opt/sonic-pi/etc/samples/vinyl_backspin.flac',
  #8: '/opt/sonic-pi/etc/samples/elec_soft_kick.flac',
  #9: '/opt/sonic-pi/etc/samples/elec_tick.flac',
  #10: '/opt/sonic-pi/etc/samples/vinyl_rewind.flac',
  #11: '/opt/sonic-pi/etc/samples/elec_twang.flac',
#}

#UNCOMMENT FOR ANIMAL SOUNDS :)

SOUND_MAPPING = {
0: '/home/pi/Desktop/New_For_Mark/1.circle.wav',
1: '/home/pi/Desktop/New_For_Mark/1.square.wav',
2: '/home/pi/Desktop/New_For_Mark/1.triangle.wav',
3: '/home/pi/Desktop/New_For_Mark/2.circle.wav',
4: '/home/pi/Desktop/New_For_Mark/2.square.wav',
5: '/home/pi/Desktop/New_For_Mark/2.triangle.wav',
6: '/home/pi/Desktop/New_For_Mark/3.circle.wav',
7: '/home/pi/Desktop/New_For_Mark/3.square.wav',
8: '/home/pi/Desktop/New_For_Mark/3.triangle.wav',
9: '/home/pi/Desktop/New_For_Mark/4.circle.wav',
10: '/home/pi/Desktop/New_For_Mark/4.square.wav',
11: '/home/pi/Desktop/New_For_Mark/4.triangle.wav',
12: '/home/pi/Desktop/New_For_Mark/5.circle.wav',
13: '/home/pi/Desktop/New_For_Mark/5.square.wav',
14: '/home/pi/Desktop/New_For_Mark/5.triangle.wav',
 }

sounds = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for key,soundfile in SOUND_MAPPING.iteritems():
        sounds[key] =  pygame.mixer.Sound(soundfile)
        sounds[key].set_volume(1);

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
           # j = random(0,14)
            if (sounds[i]):
                sounds[i].play(loops=-1)
                print cap.filtered_data(i)
        if not current_touched & pin_bit and last_touched & pin_bit:
        	print('{0} released!'.format(i))
		if (sounds[i]):
			sounds[i].fadeout(500)
			#sounds[i].stop()
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.1)

    # Alternatively, if you only care about checking one or a few pins you can
    # call the is_touched method with a pin number to directly check that pin.
    # This will be a little slower than the above code for checking a lot of pins.
    #if cap.is_touched(0):
    #    print('Pin 0 is being touched!')

    # If you're curious or want to see debug info for each pin, uncomment the
    # following lines:
    #print('\t\t\t\t\t\t\t\t\t\t\t\t\t 0x{0:0X}'.format(cap.touched()))
    #filtered = [cap.filtered_data(i) for i in range(12)]
    #print('Filt:', '\t'.join(map(str, filtered)))
    #base = [cap.baseline_data(i) for i in range(12)]
    #print('Base:', '\t'.join(map(str, base)))
