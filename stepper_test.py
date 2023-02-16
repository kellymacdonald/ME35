'''
    Stepper Motor interfacing with Raspberry Pi
    http:///www.electronicwings.com
'''
import RPi.GPIO as GPIO
from time import sleep
import sys

#assign GPIO pins for motor
motor_channel = (18,17,27,22)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#for defining more than 1 GPIO channel as input/output use
GPIO.setup(motor_channel, GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


while True:
    steps = int(input('Enter integer number of steps: '))
    i = 0
    while i < steps:
        if i % 4 == 1: 
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        elif i % 4 == 2: 
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        elif i % 4 == 3:
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        else:
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        i = i + 1
        sleep(0.01)
        

    # try:
    #     if(motor_direction == 'c'):
    #         print('motor running clockwise\n')
    #         GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    #         sleep(0.01)
    #         GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
    #         sleep(0.01)
    #         GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    #         sleep(0.01)
    #         GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
    #         sleep(0.01)

    #     elif(motor_direction == 'a'):
    #         print('motor running anti-clockwise\n')
    #         GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    #         sleep(0.02)
    #         GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
    #         sleep(0.02)
    #         GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    #         sleep(0.02)
    #         GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
    #         sleep(0.02)

            
    # #press ctrl+c for keyboard interrupt
    # except KeyboardInterrupt:
    #     #query for setting motor direction or exit
    #     motor_direction = input('select motor direction a=anticlockwise, c=clockwise or q=exit: ')
    #     #check for exit
    #     if(motor_direction == 'q'):
    #         print('motor stopped')
    #         sys.exit(0)