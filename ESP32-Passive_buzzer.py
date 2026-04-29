# Passive Buzzer (ESP32 / MakePico) - Improved Version
# 1. Uses PWM duty_u16() for MicroPython
# 2. Adds silence between notes
# 3. Handles rests (0 frequency)
# 4. Prevents deinit during playback

from machine import Pin, PWM
from time import sleep

# Passive buzzer pin
BUZZER_PIN = 25

# Create PWM object
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)   # Start silent

# Notes (Hz)
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

# Song: Twinkle Twinkle
melody = [
    C4, C4, G4, G4, A4, A4, G4,
    F4, F4, E4, E4, D4, D4, C4
]

beats = [
    0.4,0.4,0.4,0.4,0.4,0.4,0.8,
    0.4,0.4,0.4,0.4,0.4,0.4,0.8
]

# Play one tone
def play_tone(freq, duration):
    if freq == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(freq)
        buzzer.duty_u16(30000)   # volume

    sleep(duration)

    # short pause between notes
    buzzer.duty_u16(0)
    sleep(0.05)

# Main loop
try:
    while True:
        for i in range(len(melody)):
            play_tone(melody[i], beats[i])
        sleep(1)

except KeyboardInterrupt:
    buzzer.deinit()
    print("Stopped")
