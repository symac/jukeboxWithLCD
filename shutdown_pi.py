#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os
pinNumber = 11


GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNumber, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def my_callback(channel):
	global start
	global end
	global pinNumber

	if GPIO.input(pinNumber) == 1:
		start = time.time()
	if GPIO.input(pinNumber) == 0:
		end = time.time()
		elapsed = end - start
		# On ne 
		if elapsed > 1:
			print "Time elapsed > 1, we will shutdown"
			os.system("sudo shutdown -h now")
		else:
			print "Erreur de detection ?"

GPIO.add_event_detect(pinNumber, GPIO.BOTH, callback=my_callback, bouncetime=200) 
while (1):
	time.sleep(1)
