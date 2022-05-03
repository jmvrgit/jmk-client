#!/usr/bin/env python
import serial
import os
from time import sleep

#init values
moisture=""
deviceId="1"
watered=0

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #select serial USB of arduino
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0: #if serial buffer is not empty
            moisture = ser.readline().decode('utf-8').rstrip() #decode serial
            percentage = (int(moisture)/1024)*100

            if (percentage < 50):
                GPIO.output(11, GPIO.LOW) # turn on pump
                watered = 1
            else:
                GPIO.output(11, GPIO.HIGH) # keep pump off
                watered = 0

            #send data to server
            runupload = "node ./index.js " + str(moisture) + " " + str(deviceId) + " " + str(watered) 
            os.system(runupload)
