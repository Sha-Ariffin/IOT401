# TM1637 4-Digit 7-Segment Display
# Example: Digital Clock Style Counter (MM:SS)
# ESP32 / MakePico / MicroPython
# CLK -> GPIO16
# DIO -> GPIO17

from micropython import const
from machine import Pin
from time import sleep, sleep_us

# TM1637 Commands
TM1637_CMD1 = const(64)
TM1637_CMD2 = const(192)
TM1637_CMD3 = const(128)
TM1637_DSP_ON = const(8)

# Digit segments
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

    def clock(self, minute, second):
        d1 = digits[minute // 10]
        d2 = digits[minute % 10] | 0x80   # colon ON
        d3 = digits[second // 10]
        d4 = digits[second % 10]

        self.show([d1, d2, d3, d4])

# MAIN PROGRAM
tm = TM1637(clk=16, dio=17)

while True:
    for minute in range(100):       # 00 to 99
        for second in range(60):   # 00 to 59
            tm.clock(minute, second)
            sleep(1)