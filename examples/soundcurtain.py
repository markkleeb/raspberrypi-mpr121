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

pygame.mixer.pre_init(44100, -16, 27, 512)
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


earth_cyma = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_cyma_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_cyma_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_cyma_loop3.wav',
 }

sounds1 = [0,0,0]

for key,soundfile in earth_cyma.iteritems():
        sounds1[key] =  pygame.mixer.Sound(soundfile)
        sounds1[key].set_volume(0);
        sounds1[key].play(loops=-1)

earth_grain = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_grain_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_grain_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_grain_loop3.wav',
 }

sounds2 = [0,0,0]

for key,soundfile in earth_grain.iteritems():
        sounds2[key] =  pygame.mixer.Sound(soundfile)
        sounds2[key].set_volume(0);
        sounds2[key].play(loops=-1)

earth_sono = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_sono_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_sono_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/EARTH_sono_loop3.wav',
 }

sounds3 = [0,0,0]

for key,soundfile in earth_sono.iteritems():
        sounds3[key] =  pygame.mixer.Sound(soundfile)
        sounds3[key].set_volume(0);
        sounds3[key].play(loops=-1)

fire_cyma = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_cyma_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_cyma_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_cyma_loop3.wav',
 }

sounds4 = [0,0,0]

for key,soundfile in fire_cyma.iteritems():
        sounds4[key] =  pygame.mixer.Sound(soundfile)
        sounds4[key].set_volume(0);
        sounds4[key].play(loops=-1)

fire_grain = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_grain_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_grain_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_grain_loop3.wav',
 }

sounds5 = [0,0,0]

for key,soundfile in fire_grain.iteritems():
        sounds5[key] =  pygame.mixer.Sound(soundfile)
        sounds5[key].set_volume(0);
        sounds5[key].play(loops=-1)

fire_sono = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_sono_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_sono_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/FIRE_sono_loop3.wav',
 }

sounds6 = [0,0,0]

for key,soundfile in fire_sono.iteritems():
        sounds6[key] =  pygame.mixer.Sound(soundfile)
        sounds6[key].set_volume(0);
        sounds6[key].play(loops=-1)


water_cyma = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_cyma_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_cyma_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_cyma_loop3.wav',
 }

sounds7 = [0,0,0]

for key,soundfile in water_cyma.iteritems():
        sounds7[key] =  pygame.mixer.Sound(soundfile)
        sounds7[key].set_volume(0);
        sounds7[key].play(loops=-1)

water_grain = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_grain_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_grain_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_grain_loop3.wav',
 }

sounds8 = [0,0,0]

for key,soundfile in water_grain.iteritems():
        sounds8[key] =  pygame.mixer.Sound(soundfile)
        sounds8[key].set_volume(0);
        sounds8[key].play(loops=-1)

water_sono = {
0: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_sono_loop1.wav',
1: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_sono_loop2.wav',
2: '/home/pi/Adafruit_Python_MPR121/examples/loops/WATER_sono_loop3.wav',
 }

sounds9 = [0,0,0]

for key,soundfile in water_sono.iteritems():
        sounds9[key] =  pygame.mixer.Sound(soundfile)
        sounds9[key].set_volume(0);
        sounds9[key].play(loops=-1)


sounds = [sounds1, sounds2, sounds3, sounds4, sounds5, sounds6, sounds7, sounds8, sounds9]

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
            j = random(0,3)
            if (sounds[i][j]):
                sounds[i][j].set_volume(1)
                print cap.filtered_data(i)
        if not current_touched & pin_bit and last_touched & pin_bit:
        	print('{0} released!'.format(i))
        for j in sounds[i]:
          sounds[i][j].set_volume(0)
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
