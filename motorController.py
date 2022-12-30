# Parts of the code in this class is inspired from the link below
# https://ben.akrin.com/driving-a-28byj-48-stepper-motor-uln2003-driver-with-a-raspberry-pi/

import RPi.GPIO as GPIO
import time


class MotorController:
    # all class attributes below are constant values

    # time between each step on the motor
    step_sleep: float = 0.002

    # defining stepper motor sequence
    step_sequence = [[1, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 1, 1],
                     [1, 0, 0, 1]]

    step_count_360_deg: int = 2048  # 360° / (11,25° * (1/64)) = 2.048 steps
    step_count_180_deg: int = int(step_count_360_deg / 2)
    step_count_90_deg: int = int(step_count_360_deg / 4)

    clockwise: str = 'clockwise'
    antiClockwise: str = 'antiClockwise'

    def __init__(self, motor: str) -> None:
        if motor == 'front':
            self.in1: int = 33
            self.in2: int = 37
            self.in3: int = 7
            self.in4: int = 8

        elif motor == 'right':
            self.in1: int = 10
            self.in2: int = 11
            self.in3: int = 12
            self.in4: int = 13

        elif motor == 'down':
            self.in1: int = 15
            self.in2: int = 16
            self.in3: int = 18
            self.in4: int = 19

        elif motor == 'left':
            self.in1: int = 21
            self.in2: int = 22
            self.in3: int = 23
            self.in4: int = 24

        elif motor == 'back':
            self.in1: int = 26
            self.in2: int = 29
            self.in3: int = 31
            self.in4: int = 32

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        # initializing
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

        self.motor_pins = [self.in1, self.in2, self.in3, self.in4]

    def rotate(self, move: str) -> None:
        # default values if move is only assigned the side (i.e. 'D', 'F', 'R', 'B' or 'L')
        motor_steps: int = MotorController.step_count_90_deg
        direction: str = MotorController.clockwise

        if move[-1] == '\'':
            direction = MotorController.antiClockwise

        elif move[-1] == '2':
            motor_steps = MotorController.step_count_180_deg

        motor_step_counter: int = 0

        for i in range(motor_steps):
            for count, pin in enumerate(self.motor_pins):
                GPIO.output(pin, MotorController.step_sequence[motor_step_counter][count])
            
            if direction == MotorController.clockwise:
                motor_step_counter = (motor_step_counter - 1) % 4

            elif direction == MotorController.antiClockwise:
                motor_step_counter = (motor_step_counter + 1) % 4

            time.sleep(MotorController.step_sleep)
        
        self.__cleanup_pins()

    def __cleanup_pins(self) -> None:
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
