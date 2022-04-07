#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os

#Definitions

def zero_to_infinity():
	i = 0
	while True:
		time.sleep(0.1)
		yield i
		i += 1

for x in zero_to_infinity():
#Defined pins
	try:
		GPIO.setmode(GPIO.BOARD)
		pinTrigger = 7
		pinEcho = 11
		GPIO.setup(pinTrigger, GPIO.OUT)
		GPIO.setup(pinEcho, GPIO.IN)

		GPIO.output(pinTrigger, GPIO.LOW)
		GPIO.output(pinTrigger, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(pinTrigger, GPIO.LOW)

#Code
		while GPIO.input(pinEcho)==0:
			pulseStartTime = time.time()
		while GPIO.input(pinEcho)==1:
			pulseEndTime = time.time()
		pulseDuration = pulseEndTime - pulseStartTime
		distance = round(pulseDuration * 17150, 2)
		accurate_distance = distance/100

		with open("A_distance.txt", "a") as f:
			f.write((str(accurate_distance)))
			f.write('\n')

		if accurate_distance < 2:
			print("Warning! : Safety Zone limit exceeded! Distance: %.2f m" % (distance/100))
		else:
			print("Distance: %.2f m" % (distance/100))
	finally:
	    GPIO.cleanup()

