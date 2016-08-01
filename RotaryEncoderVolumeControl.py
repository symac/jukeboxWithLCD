#!/usr/local/bin/python


# depends on: http://pyalsaaudio.sourceforge.net
# sudo apt-get install python-alsaaudio

# KY040 Rotary Encoder + Raspberry Pi (model A+)
# ===
# + (5V) e.g. GPIO.BOARD 17
# BTN is on GPIO.BOARD 13
# GND e.g. GPIO.BOARD 14
# B (DT) is on GPIO.BOARD 10
# A (CLK) is on GPIO.BOARD 8

import sys
import time
import alsaaudio
import RPi.GPIO as GPIO
from RotaryEncoder import RotaryEncoder

# (!) use BOARD NRs for PINs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Volume:

	def __init__(self):
		self.mixer = alsaaudio.Mixer(control='PCM')
	
	def get_volume(self):
		return self.mixer.getvolume('playback')[0]

	def set_volume(self, percentage):
		if percentage < 0:
			percentage = 0
		elif percentage > 100:
			percentage = 100
		
		self.mixer.setvolume(percentage)
		time.sleep(.2)
	
	def volume_up(self):
		self.set_volume(self.get_volume() + 5)
		print "Volume UP (%s)" % self.get_volume()

		
	def volume_down(self):
		self.set_volume(self.get_volume() - 5)
		print "Volume DOWN (%s)" % self.get_volume()
		
	def callback(self, direction, btn_pressed):
		if direction == RotaryEncoder.DIRECTION_CLOCKWISE:
			self.volume_up()
		elif direction == RotaryEncoder.DIRECTION_COUNTERCLOCKWISE:
			self.volume_down()
def main_loop():
    while True:
        time.sleep(0.5)
		
if __name__ == '__main__':
	try:
		vol = Volume()
		enc = RotaryEncoder(8, 10, 13, vol.callback)
		main_loop()
	except KeyboardInterrupt:
		print >> sys.stderr, '\nExiting by user request.\n'
		sys.exit(0)
