#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  版本：V2.0
#  author: zhulin
# Onboard LED running light experiment
#---------------------------------------
from machine import Pin
from utime import sleep

# Define LED Pins
led=[16,17,18,19,23,5,2,22]
leds = [Pin(led[i],Pin.OUT) for i in range(0,8)]

# Program Starts
if __name__ == '__main__':
    # Loop statement
    while True:
        for n in range(0,8):# Light up in sequence
            leds[n].value(1)
            sleep(0.05)
        for n in range(0,8): # Turn off in turn
            leds[n].value(0)
            sleep(0.05)
