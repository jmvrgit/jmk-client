#!/usr/bin/env python
import serial
import os
from time import sleep

#init values
moisture=""
deviceId="1"
watered=0

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #select serial USB
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            moisture = ser.readline().decode('utf-8').rstrip() #decode serial
            print(moisture)

            if (moisture < 50):
                GPIO.output(11, GPIO.LOW) # turn on pump
                watered = 1
            else:
                GPIO.output(11, GPIO.HIGH) # keep pump off
                watered = 0

            #send data to server
            runupload = "node ./index.js " + str(moisture) + " " + str(deviceId) + " " + str(watered) 
            os.system(runupload)