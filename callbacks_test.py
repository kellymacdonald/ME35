import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def callback():
    print("Limit switch pressed")
    sleep(0.02)

while True:
    if GPIO.input(29) == 1:
        callback()
    else:
        print("-")