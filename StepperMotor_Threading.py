# Messy code to run 2 stepper motors simultaneously with different step inputs per motor

# Written by Briana Bouchard

 

import RPi.GPIO as GPIO

import time

import threading

import board

from adafruit_apds9960.apds9960 import APDS9960

from adafruit_apds9960 import colorutility

 

i2c = board.I2C()  # uses board.SCL and board.SDA

# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

apds = APDS9960(i2c)

apds.enable_color = True

 

# Set the GPIO mode

#GPIO.setmode(GPIO.BCM)

 

# Define direction values

cw = 1

ccw = 0

 

def get_color():

    while not apds.color_data_ready:

        time.sleep(0.005)

    return apds.color_data

 

def setMotor(motor, current_step, delay):

# This function provides the step sequence

 

    if current_step == 0:

        GPIO.output(motor[0],GPIO.HIGH)

        GPIO.output(motor[1],GPIO.LOW)

        GPIO.output(motor[2],GPIO.HIGH)

        GPIO.output(motor[3],GPIO.LOW)

        time.sleep(delay)

 

    elif current_step == 1:

        GPIO.output(motor[0],GPIO.LOW)

        GPIO.output(motor[1],GPIO.HIGH)

        GPIO.output(motor[2],GPIO.HIGH)

        GPIO.output(motor[3],GPIO.LOW)

        time.sleep(delay)

 

    elif current_step == 2:

        GPIO.output(motor[0],GPIO.LOW)

        GPIO.output(motor[1],GPIO.HIGH)

        GPIO.output(motor[2],GPIO.LOW)

        GPIO.output(motor[3],GPIO.HIGH)

        time.sleep(delay)

       

    elif current_step == 3:

        GPIO.output(motor[0],GPIO.HIGH)

        GPIO.output(motor[1],GPIO.LOW)

        GPIO.output(motor[2],GPIO.LOW)

        GPIO.output(motor[3],GPIO.HIGH)

        time.sleep(delay)

 

def moveSteps(motor: list[int], input_steps, steps_rev, speed):    

# This function tracks the number of steps remaining based on the step input and the loop cycles

 

    current_step = 0

    delay = 60/(steps_rev*speed)

   

    # Determines the direction based on sign of input_steps

    if input_steps > 0:

        direction = ccw

    if input_steps < 0:

        direction = cw

   

    # Track and set current step iteration

    for steps_remaining in range (abs(input_steps), 0, -1):

        if direction == cw:

            if current_step >= 0 and current_step < 3:

                current_step = current_step + 1

            elif current_step == 3:

                current_step = 0

        if direction == ccw:

            if current_step <= 3 and current_step > 0:

                current_step = current_step - 1

            elif current_step == 0:

                current_step = 3

               

        setMotor(motor, current_step, delay)

       

    print("Stepping complete! Your motor completed "  + str(abs(input_steps)) + " steps at " + str(speed)+ " revolutions per minute")

 

class Stepper (threading.Thread):

    def __init__(self, threadID, name, motor, steps, steps_rev, speed):

        threading.Thread.__init__(self)

        self.threadID = threadID

        self.name = name

        self.motor = motor

        self.steps = steps

        self.steps_rev = steps_rev

        self.speed = speed

 

    def run(self):

        print("Starting " + str(self.name))

 

        # Set GPIO pins for motors as outputs

        pin1 = 0

        for pin1 in range(0,4,1):

            GPIO.setup(self.motor[pin1], GPIO.OUT)

       

        moveSteps(self.motor,self.steps,self.steps_rev,self.speed)

       

        print("Exiting " + str(self.name))