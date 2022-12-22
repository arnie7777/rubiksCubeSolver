#  https://roboticsbackend.com/raspberry-pi-control-led-python-3/

import RPi.GPIO as GPIO
from time import sleep


class LedController:
    green_led_pin: int = 36
    red_led_pin: int = 38
    red_led_blink: bool = True

    @staticmethod
    def setup() -> None:
        GPIO.setup(LedController.green_led_pin, GPIO.OUT)
        GPIO.setup(LedController.red_led_pin, GPIO.OUT)

    @staticmethod
    def turn_on_green() -> None:
        GPIO.output(LedController.green_led_pin, GPIO.HIGH)

    @staticmethod
    def turn_off_green() -> None:
        GPIO.output(LedController.green_led_pin, GPIO.LOW)

    @staticmethod
    def start_red_blink() -> None:
        while LedController.red_led_blink:
            GPIO.output(LedController.red_led_pin, GPIO.HIGH)
            sleep(0.3)
            GPIO.output(LedController.red_led_pin, GPIO.LOW)
            sleep(0.3)

    @staticmethod
    def stop_red_blink() -> None:
        LedController.red_led_blink = False
