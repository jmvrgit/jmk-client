#!/usr/bin/env python
import serial
import os
from time import sleep
import RPi.GPIO as GPIO

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
            print(str(percentage) + "% moisture")
            if (percentage < 50):
                GPIO.output(11, GPIO.LOW) # turn on pump
                watered = 1
                print ("turn pump ON")
            else:
                GPIO.output(11, GPIO.HIGH) # keep pump off
                watered = 0
                print ("Keep Pump OFF")

            #send data to server
            runupload = "node ./index.js " + str(moisture) + " " + str(deviceId) + " " + str(watered) 
            os.system(runupload)
            print ("Upload Complete")
