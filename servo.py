# !/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Nov 2021
# This program initiates a rotational cycle for
#   the servo at a degree of 180 and back to 0 every 
#   one second interval

import time
import board
import pwmio
from adafruit_motor import servo


# create a PWMOut object on Pin GP16.
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 180
    time.sleep(1.0)
    my_servo.angle = 0
    time.sleep(1.0)
