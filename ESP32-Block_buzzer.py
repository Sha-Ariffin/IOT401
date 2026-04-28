#!/usr/bin/env python3
#  author: zhulin
#  Buzzer
from machine import Pin
from time import sleep

makerobo_Buzzer = 27

# GPIO function
def makerobo_setup(pin):
    global makerobo_BuzzerPin
    global buzzer
    makerobo_BuzzerPin = pin
    buzzer=Pin(makerobo_BuzzerPin,Pin.OUT)       # Set output mode
    buzzer.value(1)                              # Set the buzzer to high level

#  turn on buzzer
def makerobo_buzzer_on():
    buzzer.value(0)         #triggered by a low level,and it make sound.
# Turn off the buzzer
def makerobo_buzzer_off():
    buzzer.value(1)         # Set to high level to turn off

# Control the buzzer to sound
def makerobo_beep(x):
    makerobo_buzzer_on()     # Turn on
    sleep(x)            # Delay time
    makerobo_buzzer_off()    # Turn off
    sleep(x)            # 延时时间

# Loop Function
def loop():
    while True:
        makerobo_beep(0.5) #delay time of 500mm.

# Program starts
if __name__ == '__main__':
    makerobo_setup(makerobo_Buzzer) # Define GPIOpin
    loop()                          # Loop


