import network
import time

ssid = "WIFI"
password = "Password#"

wlan = network.WLAN(network.STA_IF)

# Reset WiFi state
wlan.active(False)
time.sleep(1)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to WiFi...")
    wlan.connect(ssid, password)

    timeout = 10  # seconds
    start = time.time()

    while not wlan.isconnected():
        if time.time() - start > timeout:
            print("Connection timeout!")
            break
        time.sleep(1)

if wlan.isconnected():
    print("Connected:", wlan.ifconfig())
else:
    print("Failed to connect")