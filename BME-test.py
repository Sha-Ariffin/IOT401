from machine import Pin, SoftI2C
import bme280

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21)
)

print(i2c.scan())

sensor = bme280.BME280(i2c=i2c)

print(sensor.temperature)
print(sensor.humidity)
print(sensor.pressure)