#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [4,5,6,12,13,16,18,19,21,22]
for led in leds:
     GPIO.setup(led,GPIO.OUT)
     GPIO.output(led,GPIO.LOW)

while True:
    for led in leds:
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(led,GPIO.LOW)
        


