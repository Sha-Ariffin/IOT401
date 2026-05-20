# ESP32 ESP-NOW RECEIVER + OLED

from machine import Pin, SoftI2C
import network
import espnow
import ssd1306

# I2C Configuration
SDA_PIN = 21
SCL_PIN = 22

i2c = SoftI2C(
    scl=Pin(SCL_PIN),
    sda=Pin(SDA_PIN),
    freq=100000
)

# OLED Setup

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# WiFi Setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Receiver MAC:", wlan.config('mac'))

# ESP-NOW Setup
e = espnow.ESPNow()
e.active(True)

# Initial OLED Message
oled.fill(0)
oled.text("ESP-NOW RECEIVER", 0, 0)
oled.text("Waiting...", 0, 20)
oled.show()

print("Waiting for data...")

# Receive Loop
while True:

    host, msg = e.recv()

    if msg:

        # Convert bytes to string
        received_msg = msg.decode()

        # Print in Shell
        print("Received:", received_msg)

        # OLED Display
        oled.fill(0)

        oled.text("DATA RECEIVED", 0, 0)

        # Display full message
        oled.text(received_msg[:20], 0, 20)

        # If message is long, continue next line
        if len(received_msg) > 20:
            oled.text(received_msg[20:40], 0, 35)

        oled.show()