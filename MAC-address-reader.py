# ESP32 MAC Address Reader in MicroPython
# Run using Thonny

import network
import ubinascii

# Activate Wi-Fi Station interface
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Get MAC address
mac = wifi.config('mac')

# Convert binary MAC to readable format
mac_address = ubinascii.hexlify(mac, ':').decode()

print("[DEFAULT] ESP32 Board MAC Address:", mac_address)