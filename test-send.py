#!/usr/bin/env python
import os
# import RPi.GPIO as GPIO
# import serial
from time import sleep
import random

# GPIO.setwarnings(False) 
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)

moisture=""
deviceId="1"
watered=""

def main():
    print ("Sending Data")
    # GPIO.output(11, GPIO.HIGH)

    #random number generator for testing
    moisture = random.randint(0,100) + round(random.random(),2)

    #arduino
    # if ser.in_waiting > 0:
    # moisture = ser.readline().decode('utf-8').rstrip()
    # moisture = round(moisture,2)

    if (moisture < 50):
        # GPIO.output(11, GPIO.LOW)
        watered = 1
    else:
        # GPIO.output(11, GPIO.HIGH)
        watered = 0
    

    runupload = "node ./index.js " + str(moisture) + " " + str(deviceId) + " " + str(watered)
    os.system(runupload)
    print(runupload)
    sleep(1)

while True:
    main()