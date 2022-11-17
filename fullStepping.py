#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from timer import Timer

time.sleep(5)
 
in1 = 17
in2 = 18
in3 = 27
in4 = 22
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_count = 2048  # 360° / (11,25° * (1/64)) = 2.048 steps
step_count_180_deg = step_count / 2
step_count_90_deg = step_count / 4
 
direction = True # True for clockwise, False for counter-clockwise
 
# defining stepper motor sequence
step_sequence = [[1,1,0,0],
                 [0,1,1,0],
                 [0,0,1,1],
                 [1,0,0,1]]
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
 
 
motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0
 
 
def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
 
my_timer = Timer()
my_timer.start()

try:
    i = 0
    for i in range(int(step_count_90_deg)):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction == True:
            motor_step_counter = (motor_step_counter - 1) % 4
        elif direction == False:
            motor_step_counter = (motor_step_counter + 1) % 4
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )

except KeyboardInterrupt:
    print('Just before cleanup in exception')
    cleanup()
    exit( 1 )

print(my_timer.stop())
 
print('Just before cleanup')
cleanup()
exit( 0 )
