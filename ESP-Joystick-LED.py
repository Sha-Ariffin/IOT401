# ESP32 + Joystick + OLED Display + LED
# Detect LEFT, RIGHT, UP, DOWN

from machine import Pin, ADC, SoftI2C
import ssd1306
import time

# OLED Configuration
i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Joystick Configuration
vrx = ADC(Pin(32))
vry = ADC(Pin(33))

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

vrx.width(ADC.WIDTH_12BIT)
vry.width(ADC.WIDTH_12BIT)

# LED Configuration
greenLED = Pin(25, Pin.OUT)
redLED   = Pin(26, Pin.OUT)
whiteLED = Pin(27, Pin.OUT)
blueLED  = Pin(14, Pin.OUT)

# Thresholds
LEFT_THRESHOLD   = 1000
RIGHT_THRESHOLD  = 4000
UP_THRESHOLD     = 1000
DOWN_THRESHOLD   = 4000

# Function: Turn OFF all LEDs
def all_led_off():
    greenLED.off()
    redLED.off()
    whiteLED.off()
    blueLED.off()

# Main Loop
while True:

    xValue = vrx.read()
    yValue = vry.read()

    direction = "CENTER"

    # Turn OFF all LEDs first
    all_led_off()

    # LEFT
    if xValue < LEFT_THRESHOLD:
        direction = "LEFT"
        greenLED.on()

    # RIGHT
    elif xValue > RIGHT_THRESHOLD:
        direction = "RIGHT"
        redLED.on()

    # UP
    elif yValue < UP_THRESHOLD:
        direction = "UP"
        whiteLED.on()

    # DOWN
    elif yValue > DOWN_THRESHOLD:
        direction = "DOWN"
        blueLED.on()

    # Serial Output
    print("-------------------")
    print("X =", xValue)
    print("Y =", yValue)
    print("Direction =", direction)

    # OLED Display
    oled.fill(0)

    oled.text("JOYSTICK TEST", 0, 0)
    oled.text("X: {}".format(xValue), 0, 20)
    oled.text("Y: {}".format(yValue), 0, 35)
    oled.text(direction, 0, 50)

    oled.show()

    time.sleep(0.2)