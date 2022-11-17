import RPi.GPIO as GPIO
import time

class MotorController:
    mode_has_been_set: bool = False

    def __init__(self, motor: str) -> None:
        if motor == 'right':
            self.in1: int = 11
            self.in2: int = 12
            self.in3: int = 13
            self.in4: int = 15

        # else if left etc.

        self.step_sleep: float = 0.002

        """
        self.step_count = 2048  # 360° / (11,25° * (1/64)) = 2.048 steps
        self.step_count_180_deg = step_count / 2
        self.step_count_90_deg = step_count / 4
        """

        # defining stepper motor sequence
        self.step_sequence = [[1,1,0,0],
                              [0,1,1,0],
                              [0,0,1,1],
                              [1,0,0,1]]

        # setting up
        if not mode_has_been_set:
            GPIO.setmode(GPIO.BOARD)
            mode_has_been_set = True

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
        motor_steps: int = 510  # 90 degrees
        direction: str = 'clockwise'

        if move[-1] == '\'':
            direction = 'anticlockwise'

        elif move[-1] == '2':
            motor_steps = 1020  # 180 degrees

        motor_step_counter: int = 0

        for i in range(motor_steps):
            for count, pin in enumerate(self.motor_pins):
                GPIO.output(pin, self.step_sequence[motor_step_counter][count] )
            if direction == 'clockwise':
                motor_step_counter = (motor_step_counter - 1) % 4
            elif direction == 'anticlockwise':
                motor_step_counter = (motor_step_counter + 1) % 4


    def cleanup(self) -> None:
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.cleanup()
