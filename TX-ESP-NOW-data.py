# ESP32 + BME280 + OLED + ESP-NOW
# TRANSMITTER CODE

from machine import Pin, SoftI2C
import network
import espnow
import time
import bme280
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

# BME280 Setup
bme = bme280.BME280(i2c=i2c)

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

    # Read Sensor Values
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure

    # Create Message
    message = "Temp:{} Hum:{} Pres:{}".format(
        temp,
        hum,
        pres
    )

    # Send Message
    ok = e.send(peer, message)

    if ok:
        print("Message sent")
    else:
        print("Send failed")

    # OLED Display
    oled.fill(0)
    oled.text("BME280 READINGS", 0, 0)
    oled.text("Temp:", 0, 20)
    oled.text(str(temp), 50, 20)
    oled.text("Hum:", 0, 35)
    oled.text(str(hum), 50, 35)
    oled.text("Pres:", 0, 50)
    oled.text(str(pres), 50, 50)

    oled.show()
    time.sleep(10)