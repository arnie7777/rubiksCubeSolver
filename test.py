import RPi.GPIO as GPIO


class Test:
    @staticmethod
    def set_mode() -> None:
        GPIO.setmode(GPIO.BOARD)

    @staticmethod
    def cleanup() -> None:
        GPIO.cleanup()
