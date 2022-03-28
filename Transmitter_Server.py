#!/usr/bin/python3


import RPi.GPIO as GPIO
import time
import socket
import os


#    with open('stream2.txt') as f:
#       storedValue = str(f.read())
#with open('stream2.txt') as f:
#    for line in f:
#        storedValue = str(print(line.strip()))

host = '192.168.1.222' #IP of host server
port = 5560  #Choosen port to use session

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Setting up server please wait...")
    try:
        s.bind((host, port)) #binding ip:port = socket
    except socket.error as msg: #error message
        print(msg)
    print("Server is up!")
    return s #means return ongoing session - refer to s

def setupConnection():
    s.listen(8) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    process_out = "./DistanceSensor.py >> stream.txt"
    conversion = "sed -e :a -e '$q;N;21,$D;ba' stream.txt > stream2.txt"
    printing = "cat stream2.txt"
    os.system(process_out)
    os.system(conversion)
    with open('stream2.txt') as f:
        storedValue = str(f.readlines()) #reading from txt file and converting text into string
    reply = str.encode(storedValue) #encoding data string
    return reply


def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Client Disconnected")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(reply)
        print("Data has been sent!")
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break





