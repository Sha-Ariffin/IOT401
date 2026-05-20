# ESP32 + Joystick + OLED Display
# Detect LEFT, RIGHT, UP, DOWN

from machine import Pin, ADC, SoftI2C
import ssd1306
import time

# OLED Configuration
SDA_PIN = 21
SCL_PIN = 22

i2c = SoftI2C(
    scl=Pin(SCL_PIN),
    sda=Pin(SDA_PIN),
    freq=400000
)
# OLED size (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Joystick Configuration
VRX_PIN = 32
VRY_PIN = 33

# Thresholds
LEFT_THRESHOLD   = 1500
RIGHT_THRESHOLD  = 3500

UP_THRESHOLD     = 1500
DOWN_THRESHOLD   = 4500

# Configure ADC
vrx = ADC(Pin(VRX_PIN))
vry = ADC(Pin(VRY_PIN))

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

vrx.width(ADC.WIDTH_12BIT)
vry.width(ADC.WIDTH_12BIT)

# Main Loop
while True:

    # Read joystick values
    valueX = vrx.read()
    valueY = vry.read()

    horizontal = "CENTER"
    vertical = "CENTER"

    # LEFT / RIGHT
    # Horizontal detection
    if valueX < LEFT_THRESHOLD:
        horizontal = "LEFT"

    elif valueX > RIGHT_THRESHOLD:
        horizontal = "RIGHT"

    # UP / DOWN
    # Vertical detection
    if valueY < UP_THRESHOLD:
        vertical = "UP"

    elif valueY > DOWN_THRESHOLD:
        vertical = "DOWN"

# Combine direction
    if horizontal != "CENTER" and vertical != "CENTER":
        direction = vertical + "-" + horizontal

    elif horizontal != "CENTER":
        direction = horizontal

    elif vertical != "CENTER":
        direction = vertical

    else:
        direction = "CENTER"
        
    # Serial Monitor
    print("X:", valueX,
          " Y:", valueY,
          " Direction:", direction)

    # OLED Display
    oled.fill(0)
    oled.text("JOYSTICK TEST", 0, 0)
    oled.text("X: {}".format(valueX), 0, 20)
    oled.text("Y: {}".format(valueY), 0, 35)
    oled.text(direction, 0, 50)
    oled.show()

    time.sleep(0.2)