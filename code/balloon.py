import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

button = 14
balloon_1 = 2
balloon_2 = 3
balloon_3 = 4

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(ballon_1, GPIO.OUT)
GPIO.setup(ballon_2, GPIO.OUT)
GPIO.setup(balloon_3, GPIO.OUT)

touched = GPIO.LOW

print("Ready...")
i = 1
while i == 1:
    if GPIO.input(button) == touched:
        print("Button Pushed")
        sleep(1)
        GPIO.output(balloon_1, True)
        print('Balloon 1')
        sleep(5)
        GPIO.output(balloon_1, False)

        GPIO.output(balloon_2, True)
        print('Balloon 2')
        sleep(5)
        GPIO.output(balloon_2, False)

        GPIO.output(balloon_3, True)
        print('Balloon 3')
        sleep(5)
        GPIO.output(balloon_3, False)
        i += 1
    else:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(4, False)

GPIO.cleanup()
