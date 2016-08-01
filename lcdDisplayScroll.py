#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import lcddriver
import sys

# Appel du script : 
# python lcdDisplayScroll.py "chaine à afficher" lineNumber scroll
# lineNumber entre 1 et 2
# scroll = 0 pour un affichage fixe
# scroll = 1 pour un affichage qui déroule
inputString = sys.argv[1]
inputLineNumber = sys.argv[2]
inputScroll = sys.argv[3]

lcd = lcddriver.lcd()
lcd.lcd_clear()
offset = 0
print "Scroll : %s" % inputScroll
if inputScroll == "0":
	print "Ligne affichage : %s" % inputLineNumber
	if "#" in inputString:
		(line1, line2) = inputString.split("#")
		lcd.lcd_display_string(line1, 1)
		lcd.lcd_display_string(line2, 2)
	else:
		lcd.lcd_display_string(inputString, int(inputLineNumber))
else:
	songTitle = inputString + " - "
	while 1:
		if offset == len(songTitle):
			displayString = songTitle[0:16]
			offset = 1
		elif len(songTitle) - offset < 16:
			displayString = songTitle[offset:offset + 16] + songTitle[0:16-(len(songTitle) - offset)]
			offset += 1
		else:
			displayString = songTitle[offset:offset + 16]
			offset += 1
		lcd.lcd_display_string(displayString, int(inputLineNumber))
		sleep(0.15)