#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  author: zhulin
# Instructions: Ultrasonic Sensor Distance Detection Experiment
# Precautions: The ultrasonic module must be powered by 5V!
#####################################################
from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=4, echo_pin=27) # Define the Trig and Echo pins

# Loop function
def makerobo_loop():
    while True:
        us_dis = sensor.distance_cm()   # To obtain the ultrasonic distance, you can also call sensor.distance_mm()
        print (us_dis, 'cm')           # Print ultrasonic distance values
        print ('')
        sleep(0.3)                     # Delay 300ms

# Program Starts
if __name__ == "__main__":
    makerobo_loop() # Calling the loop function
