import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 14
balloon = 2

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)

print("Ready...")
GPIO.wait_for_edge(button, GPIO.FALLING)
print("Popping...")
GPIO.output(balloon, True)
sleep(10)
GPIO.output(balloon, False)
