#!/usr/bin/python3

import os
import sys


for x in range(2, 4, 1):
	process_out = "./DistanceSensor.py >> stream.txt"
	conversion = "sed -e :a -e '$q;N;21,$D;ba' stream.txt > stream2.txt"
	printing = "cat stream2.txt"
	os.system(process_out)
	os.system(conversion)
	os.system("./transmit.sh")
