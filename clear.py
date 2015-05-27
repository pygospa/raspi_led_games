#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [4,5,6,12,13,16,18,19,21,22]
for led in leds:
     GPIO.setup(led,GPIO.OUT)
     GPIO.output(led,GPIO.LOW)


