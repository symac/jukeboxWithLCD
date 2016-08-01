#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrixKeypad_RPi_GPIO import keypad
from time import sleep
import subprocess
import RPi.GPIO as GPIO
import os
from os import path


# Initialize the keypad class
kp = keypad()
ACTIVE_PROCESS=""
ACTIVE_PROCESS_LCD=""
mp3Directory = "/home/pi/mp3_wallbox/"

songsNames = {}

def digit():
    # Loop while waiting for a keypress
    r = None
    while r == None:
        r = kp.getKey()
    return r 
 

# Getting digit 1, printing it, then sleep to allow the next digit press.

# Will load all songs from the mp3 directory
def loadSongs():
	global mp3Directory, songsNames
	print "Loading songs in %s" % mp3Directory

	counter = 0	
	for f in [f for f in os.listdir(mp3Directory) if os.path.splitext(f)[1] == ".mp3"]:
		mp3Path  = "%s%s" % (mp3Directory, f)
		mp3PathReal = os.path.realpath("%s%s" % (mp3Directory, f))
		songName = os.path.basename(mp3PathReal)
		songNumber = f.replace(".mp3", "")
		songsNames[songNumber] = songName
		counter += 1
	print "%s songs loaded" % counter

def play_song(track):
	# TODO
	print "lancement de %s" % track
	if track in songsNames:
		global ACTIVE_PROCESS, mp3Directory
		if ACTIVE_PROCESS:
			ACTIVE_PROCESS.terminate()
		ACTIVE_PROCESS = subprocess.Popen(["mpg123", "%s%s.mp3" % (mp3Directory, track)])
		# Affichage du nom de la chanson sur la première ligne
		displayLcd(songsNames[track], 1, 1)
	else:
		displayLcd("Code inconnu", "1", 0)

def getNumber(inputDigits = ""):
	d = digit()
	inputDigits = str(inputDigits) + str(d)
	displayLcd("%s#> %s" % ("Votre saisie : ", inputDigits), 2, 0)
	return inputDigits

def displayLcd(inputString, line, scroll):
	global ACTIVE_PROCESS_LCD
	if ACTIVE_PROCESS_LCD:
		ACTIVE_PROCESS_LCD.terminate()
	ACTIVE_PROCESS_LCD = subprocess.Popen(["python", "lcdDisplayScroll.py", inputString, str(line), str(scroll)])


# printing out the assembled 3 digit code.
loadSongs()
displayLcd("Jukebox ok#Saisir code", 1, 0)

# on initialise le lcd

#try:
while True:
	inputDigits = getNumber()
	sleep(0.5)
	inputDigits = getNumber(inputDigits)
	sleep(0.5)
	inputDigits = getNumber(inputDigits)
	play_song(inputDigits)
	## Affichage de la chanson
	sleep(1)
#except:
#	print "Cleaning everything"
#	GPIO.cleanup()
#print "Other error or exception occurred!" 
#finally:  
#GPIO.cleanup() # this ensures a clean exit
