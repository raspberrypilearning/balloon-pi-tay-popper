import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 14
balloons = [2, 3]

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

for balloon in balloons:
    GPIO.setup(balloon, GPIO.OUT)

print("Ready...")
GPIO.wait_for_edge(button, GPIO.FALLING)
print("Popping...")
for balloon in balloons:
    print("Armed...")
    GPIO.output(balloon, True)
    sleep(5)
    GPIO.output(balloon, False)
