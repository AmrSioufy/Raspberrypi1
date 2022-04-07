#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
import os
import sys
import time
import re
import statistics

in1 = 5
in2 = 6
in3 = 26
in4 = 16
enA = 23
enB = 24
temp1=1

current_speed = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(enA,1000)
b=GPIO.PWM(enB,1000)

p.start(current_speed)
b.start(current_speed)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")


while True:
    Distance_to_txt = "sed -e :a -e '$q;N;7,$D;ba' distance.txt > distance_stream.txt"
    conversion = "sed -e :a -e '$q;N;2,$D;ba' speed.txt > speed_stream.txt"
    os.system(conversion)
    os.system(Distance_to_txt)

    with open('speed_stream.txt') as f:
        out = f.readlines() #reading from txt file
        storedSpeed = str(out) #converted list to string
        storedSpeed = re.sub('[^0-9]', '', storedSpeed) #filtered string to a value
        storedSpeed = int(storedSpeed) #converting string to int

    with open('distance_stream.txt') as f:
        d_out = f.readlines() #reading from txt file
        data = (*d_out,)
        new_list = [x[:-1] for x in data]
#        ne_list = [x[:+6] for x in new_list]
#        print(ne_list)
#        print(round(ne_list, 2))
        float_list = [int(float(x)) for x in new_list]
        #print(float_list)
        avg = sum(float_list)/len(float_list)
        print(avg)

#        storedDistance = str(data) #converted list to string
#        storedDistance = re.sub('[^0-9]','', storedDistance) #filtered string to a value
#        storedDistance = int(storedDistance) #converting string to int
#        avg_storedDistance = sum(int(storedDistance)) / 6
#    print(avg)

    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(5)

    if storedSpeed==current_speed and avg > 2:
        print("Platooning to car B")
        p.ChangeDutyCycle(25)
        b.ChangeDutyCycle(25)


    elif storedSpeed<current_speed:
        print("Decreased speed and Platooning to car B")
        p.ChangeDutyCycle(int(storedSpeed))
        b.ChangeDutyCycle(int(storedSpeed))


    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        break
