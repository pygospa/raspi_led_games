#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [4,5,6,12,13,16,18,19,21,22]

for led in leds:
     GPIO.setup(led,GPIO.OUT)
     GPIO.output(led,GPIO.LOW)


def light(t):
    for led in leds:
        if((t % 2) == 1):
            GPIO.output(led, GPIO.HIGH)
        else:
            GPIO.output(led, GPIO.LOW)
        t = t/2
    return

t = 0.125

def binary_counter():
    for j in range (0,512):
        n = 1
        m = 2
        light((m*j)/m)
        time.sleep(t)

if __name__=='__main__':
    binary_counter()
        


