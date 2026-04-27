from machine import Pin, ADC, PWM
from time import sleep, ticks_ms

# --------------------
# Pin Setup
# --------------------
SMOKE_DO = 27        # Digital output from sensor
SMOKE_AO = 34        # Analog output from sensor
BUZZER_PIN = 4       # Passive buzzer

# --------------------
# Initialize
# --------------------
smoke_digital = Pin(SMOKE_DO, Pin.IN)
smoke_analog = ADC(Pin(SMOKE_AO))
smoke_analog.atten(ADC.ATTN_11DB)

buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty(0)       # OFF initially

# --------------------
# Functions
# --------------------
def buzzer_on():
    buzzer.freq(1000)     # 1 kHz tone
    buzzer.duty(512)      # 50% duty

def buzzer_off():
    buzzer.duty(0)

def print_safe(adc):
    print("SAFE | Gas Level =", adc)

def print_danger(adc):
    print("WARNING! SMOKE DETECTED | Gas Level =", adc)

# --------------------
# Main Loop
# --------------------
last_print = 0
state = 1

while True:
    digital = smoke_digital.value()
    analog = smoke_analog.read()

    # Print every 1 sec
    if ticks_ms() - last_print > 1000:
        if digital == 1:
            print_safe(analog)
        else:
            print_danger(analog)
        last_print = ticks_ms()

    # Alarm
    if digital == 0:
        buzzer_on()
    else:
        buzzer_off()

    sleep(0.1)
