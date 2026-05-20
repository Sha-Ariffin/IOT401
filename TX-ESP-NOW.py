# ESP32 + OLED + ESP-NOW
# TRANSMITTER CODE

from machine import Pin, SoftI2C
import network
import espnow
import time
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

print("Transmitter MAC:", wlan.config('mac'))

# ESP-NOW Setup
e = espnow.ESPNow()
e.active(True)

# Receiver MAC Address
peer = b'\x08\xb6\x1f\x85\xd5\x7c'

e.add_peer(peer)

# Main Loop
while True:

    # Message to Send
    message = "Hello Weather"

    # Send Message
    ok = e.send(peer, message)

    # Print Status
    if ok:
        print("Message sent:", message)
    else:
        print("Send failed")

    # OLED Display
    oled.fill(0)

    oled.text("ESP-NOW TX", 0, 0)

    if ok:
        oled.text("Message Sent", 0, 20)
        oled.text(message, 0, 40)
    else:
        oled.text("Send Failed", 0, 20)

    oled.show()

    time.sleep(5)