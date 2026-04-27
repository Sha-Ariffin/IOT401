#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  版本：V2.0
#  author: zhulin
# Humidity sensor detection experiment
#####################################################
from machine import Pin
import dht
import utime

makerobo_pin = 27  # DHT11 Temperature and Humidity Sensor Pin Definitions

# Define GPIO pins
def makerobo_setup():
    global dht_sensor
    dht_sensor=dht.DHT11(Pin(makerobo_pin))
    utime.sleep(1)    #Pause for 1 second upon initial startup to allow the sensor to stabilize.

# loop function
def loop():
    while True:
        dht_sensor.measure()  # Calling functions from the DHT library to measure data
        T = dht_sensor.temperature()
        H = dht_sensor.humidity()
        if T is None:
            print(" sensor error")
        else:
            print('Makerobo Temp = {0:0.2f} *C'.format(T))    # Get temperature
            print('Makerobo Humidity = {0:0.2f} %'.format(H))   # Read air pressure value
        # If the delay time is too short, the DHT11 temperature and humidity sensor will not work.
        utime.sleep_ms(2500)

# Start Program
if __name__ == '__main__':
    makerobo_setup()
    loop()

