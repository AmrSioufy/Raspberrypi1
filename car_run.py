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

current_speed = 70

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(in2,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(in3,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(in4,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(enA,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(enB,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(enA,1000)
b=GPIO.PWM(enB,1000)

p.start(current_speed)
b.start(current_speed)


with open('A_speed.txt', 'w') as f:
    f.write(str(current_speed))
    f.write('\n')


print("\n")
print("The car is now running!")
print("Enjoy your collision free car ride :)")
print("\n")


while True:


#Sending list of last 6 distance results to a txt file
#Sending last speed to a txt file
    Distance_to_txt = "sed -e :a -e '$q;N;7,$D;ba' A_distance.txt > A_distance_stream.txt"
    conversion = "sed -e :a -e '$q;N;2,$D;ba' B_speed.txt > B_speed_stream.txt"
    os.system(conversion)
    os.system(Distance_to_txt)



#Fetching speed & distance txt files and converting class types to integer
    with open('B_speed_stream.txt') as f:
        out = f.readlines() #reading from txt file
        storedSpeed = str(out) #converted list to string
        storedSpeed = re.sub('[^0-9]', '', storedSpeed) #filtered string to a value
        storedSpeed = int(storedSpeed) #converting string to int

    with open('A_distance_stream.txt') as f:
        d_out = f.readlines() #reading from txt file
        data = (*d_out,)
        new_list = [x[:-1] for x in data]
        float_list = [int(float(x)) for x in new_list]
        avg = sum(float_list)/len(float_list)
        print("Average Distance Between both Cars = ",avg)

#        storedDistance = str(data) #converted list to string
#        storedDistance = re.sub('[^0-9]','', storedDistance) #filtered string to a value
#        storedDistance = int(storedDistance) #converting string to int
#        avg_storedDistance = sum(int(storedDistance)) / 6
#    print(avg)



#Motor pins is on
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(0.5)

#Decision Blocks#

#
    if storedSpeed==current_speed and avg > 2:
        print("car A and car B are both safe")
        p.ChangeDutyCycle(int(storedSpeed))
        b.ChangeDutyCycle(int(storedSpeed))


    elif storedSpeed==current_speed and avg < 2:
        print("Slightly Decreasing speed to maintain a safe distance from car B")
        p.ChangeDutyCycle(int(storedSpeed)-10)
        b.ChangeDutyCycle(int(storedSpeed)-10)

#
    elif storedSpeed==0 and avg <= 1:
        print("Car A about to collide! BRAKING!!!")
        p.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)

    elif storedSpeed<current_speed and avg < 2:
        print("Decreased speed and increasing distance from car B")
        p.ChangeDutyCycle(int(storedSpeed)-20)
        b.ChangeDutyCycle(int(storedSpeed)-20)

    elif storedSpeed<current_speed and avg > 2:
        print("Possible safety zone break! safety distance will be maintained what so ever")
        p.ChangeDutyCycle(current_speed)
        b.ChangeDutyCycle(current_speed)
#
    else:
        print("<<<  Car running safely %% No decision is required  >>>")

