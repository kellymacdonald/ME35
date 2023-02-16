# Run 2 stepper motors simultaneously with different step inputs per motor
# Written by Briana Bouchard 

from ThreadStepperLib import Stepper, get_color, moveSteps, setMotor
import RPi.GPIO as GPIO
import time


# Define the GPIO pins for the L298N motor driver
Motor1 = [18,17,27,22]
Motor2 = [5,6,26,16]
t2=time.time()

try:
    # Define the steps per revolution for the motor 
    steps_rev = 200
    # Set the thread number, thread ID, motor, number of steps to move, steps per revolution,
    # and the speed in revolutions per minute
    r, g, b, c = get_color()
    target = r

    Lsteps = 0
    Rsteps = 0

    pin1 = 0
    for pin1 in range(0,4,1):
        GPIO.setup(Motor1[pin1], GPIO.OUT)
        GPIO.setup(Motor2[pin1], GPIO.OUT)

        
    
    # Check to see if both threads are done and clean up GPIO pins when done
except KeyboardInterrupt:
    GPIO.cleanup()

while True:
    r, g, b, c = get_color()
    print(r)
    Ierror=0
    t = 0
    t_prev = 100

    Lsteps = 20
    Rsteps = 20
    kp = 0.029 #just kept trying values
    ki = 0.01  #integral

    # Calculate the error
    p_error = target - b
    #Ierror = Ierror + ki*p_error*(t - t_prev)
    # Calculate proportional component (error * KP)
    error = int(p_error * kp)
    if error < 0:
        Rsteps += abs(error)
    elif error > 0:
        Lsteps += abs(error)


    # stepper1 = Stepper(1,"Motor #1",Motor1, Lsteps, steps_rev, 20)
    # stepper2 = Stepper(2,"Motor #2",Motor2, -Rsteps, steps_rev, 20)

    # # # Start the motor threads
    # stepper1.start()
    # stepper2.start()
    moveSteps(Motor1,Lsteps,steps_rev,30)
    moveSteps(Motor2,-Rsteps,steps_rev,30)
    # while True:
    #     if stepper1.is_alive() == False and stepper2.is_alive() ==False:
    #         GPIO.cleanup()
    #         break
    t = abs(t2-time.time())
    print(Ierror)
    print(t)
#motor gets super hot because there is no turn off but it runs 
#the while loop was in the try thats why it was very slow i think 
#i also took out the stepper functions https://jckantor.github.io/CBE30338/04.01-Implementing_PID_Control_with_Python_Yield_Statement.html