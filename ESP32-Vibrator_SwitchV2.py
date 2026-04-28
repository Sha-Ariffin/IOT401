from machine import Pin
from time import sleep_ms

# Pins
VIBRATE_PIN = 26
RED_PIN   = 4
GREEN_PIN = 27

# Setup
vibrate = Pin(VIBRATE_PIN, Pin.IN, Pin.PULL_UP)
red   = Pin(RED_PIN, Pin.OUT)
green = Pin(GREEN_PIN, Pin.OUT)

# LED Functions
def led_green():
    red.value(0)
    green.value(1)
def led_red():
    red.value(1)
    green.value(0)

# Start with safe state
led_green()
print("Waiting for vibration...")

# Main loop
while True:
    sensor = vibrate.value()
    if sensor == 0:   # vibration detected
        print("VIBRATION DETECTED!")
        led_red()
        sleep_ms(500)
    else:
        led_green()
    sleep_ms(50)
