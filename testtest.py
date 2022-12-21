import RPi.GPIO as GPIO
from test import Test
from time import sleep


Test.set_mode()
GPIO.setup(36, GPIO.OUT)

GPIO.output(36, GPIO.HIGH)
sleep(1)
GPIO.output(36, GPIO.LOW)

Test.cleanup()