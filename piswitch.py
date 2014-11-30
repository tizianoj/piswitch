#!/usr/bin/python
# coding=utf-8

""" Listening on GPIO3. On Raspberry Rev2, it is listen for a 
short circuit between pins 5 and 6 """

GPIO_IN_NUMBER = 3

import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_IN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.wait_for_edge(GPIO_IN_NUMBER, GPIO.FALLING)
    GPIO.cleanup()
    subprocess.call(['shutdown -h now "System halted by GPIO action"'], shell=True)
finally:
    GPIO.cleanup()

