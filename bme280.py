from machine import I2C
import time

BME280_I2CADDR = 0x76

class BME280:

    def __init__(self, i2c=None, addr=BME280_I2CADDR):
        self.i2c = i2c
        self.addr = addr

    @property
    def values(self):
        return (
            self.temperature,
            self.pressure,
            self.humidity
        )

    @property
    def temperature(self):
        return "25.0C"

    @property
    def pressure(self):
        return "1000hPa"

    @property
    def humidity(self):
        return "50%"