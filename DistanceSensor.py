#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import random


def zero_to_infinity():
        i = 60 #Starting Speed
        while True:
                time.sleep(0.01)
                yield i
                i -= 1 #Accelerating Speed = +ve , -ve for Deceleration
                if i == 71:
                        break
                elif i == 49:
                        break
for x in zero_to_infinity():


#i = range(30, 41, 1)
#for x in i:
#   time.sleep(0.01)

#PIN Definitions
    try:
        GPIO.setmode(GPIO.BOARD)
        pinTrigger = 7
        pinEcho = 11
        pinLED = 13
        GPIO.setup(pinTrigger, GPIO.OUT)
        GPIO.setup(pinEcho, GPIO.IN)
        GPIO.setup(pinLED, GPIO.OUT)
        GPIO.output(pinTrigger, GPIO.LOW)
        GPIO.output(pinTrigger, GPIO.HIGH)
        GPIO.output(pinLED, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, GPIO.LOW)
#Code
        while GPIO.input(pinEcho)==0:
            pulseStartTime = time.time()
        while GPIO.input(pinEcho)==1:
            pulseEndTime = time.time()
        pulseDuration = pulseEndTime - pulseStartTime
        distance = round(pulseDuration * 17150, 2)
        print("Distance: %.2f m" % (distance/100))
        print("Speed:" , x ,"Km/h")
    finally:
        GPIO.cleanup()

