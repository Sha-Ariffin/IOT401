# TM1637 + DHT11 Temperature Display
# ESP32 / MakePico / MicroPython
# TM1637 CLK -> GPIO16
# TM1637 DIO -> GPIO17
# DHT11 DATA -> GPIO15

from micropython import const
from machine import Pin
from time import sleep, sleep_us
import dht

# ---------------- TM1637 SETTINGS ----------------
TM1637_CMD1 = const(64)
TM1637_CMD2 = const(192)
TM1637_CMD3 = const(128)
TM1637_DSP_ON = const(8)

digits = bytearray(b'\x3f\x06\x5b\x4f\x66\x6d\x7d\x07\x7f\x6f')

class TM1637:
    def __init__(self, clk, dio, brightness=7):
        self.clk = Pin(clk, Pin.OUT)
        self.dio = Pin(dio, Pin.OUT)
        self.brightness = brightness

    def start(self):
        self.dio.value(1)
        self.clk.value(1)
        self.dio.value(0)
        self.clk.value(0)

    def stop(self):
        self.clk.value(0)
        self.dio.value(0)
        self.clk.value(1)
        self.dio.value(1)

    def write_byte(self, b):
        for i in range(8):
            self.clk.value(0)
            self.dio.value((b >> i) & 1)
            sleep_us(5)
            self.clk.value(1)
            sleep_us(5)

        self.clk.value(0)
        self.dio.value(1)
        self.clk.value(1)
        sleep_us(5)
        self.clk.value(0)

    def show(self, data):
        self.start()
        self.write_byte(TM1637_CMD1)
        self.stop()

        self.start()
        self.write_byte(TM1637_CMD2)

        for i in data:
            self.write_byte(i)

        self.stop()

        self.start()
        self.write_byte(TM1637_CMD3 | TM1637_DSP_ON | self.brightness)
        self.stop()

    def number(self, num):
        num = max(0, min(num, 9999))
        s = "{:0>4d}".format(num)

        data = []
        for c in s:
            data.append(digits[int(c)])

        self.show(data)

# ---------------- MAIN PROGRAM ----------------

tm = TM1637(clk=16, dio=17)
sensor = dht.DHT11(Pin(15))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()

        print("Temperature:", temp, "C")

        tm.number(temp)   # Example: 0027 = 27°C

    except:
        print("Sensor Error")

    sleep(2)