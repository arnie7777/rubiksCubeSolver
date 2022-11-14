#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
 
in1 = 17
in2 = 18
in3 = 27
in4 = 22
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
 
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
 
direction = True # True for clockwise, False for counter-clockwise
 
# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
 
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
motor_step_counter = 0 ;
 
 
def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
 
 
# the meat
try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
 
except KeyboardInterrupt:
    cleanup()
    exit( 1 )
 
print('Just before cleanup')
cleanup()
exit( 0 )








"""
from time import sleep
#from cubeSolver import CubeSolver
from algConverter import AlgConverter
from timer import Timer

def main():
    #Using timer example:
    my_timer = Timer()
    input('Press any key to start timer!')
    my_timer.start()
    input('Press any key to stop timer!')
    solved_time = my_timer.stop()
    print(solved_time)


    #Using cubeSolver example
    solver = CubeSolver()
    
    #Order is U, D, F, R, B, L (easier to follow than the kociemba library order)
    cube = ('LBBUUDDDULFULDFLUBFRFBFLBDBRBLFRLRRDURFBBDRFFURRLLUDUD')
    #Change order to what the kociemla library accepts (which is U, R, F, D, L, B)
    cube = cube[0:9] + cube[27:36] + cube[18:27] + cube[9:18] + cube[45:54] + cube[36:45]
    
    solution = solver.solve(cube)
    print(solution)
    #TODO
    #When the user will enter the cube as imput, we want to do something like the following:
    #ask user to enter which side is top and which is front
    #tell user (with picture maybe) to order from top -> bottom/down -> front -> right -> back -> left
    #make it such that the input color buttons tell the program the right side
    #e.g. the user says - top: white, front: red, right: blue, then make the white button give 'U' to the program, red gives 'F', yellow gives 'D' and so on


    #Using algConverter example
    converter = AlgConverter()
    converted_moves_one = converter.convert_to_u('U')
    print(converted_moves_one)
    converter.clear_converted_moves()

    converted_moves_two = converter.convert_to_u('U\'')
    print(converted_moves_two)
    converter.clear_converted_moves()

    converted_moves_three = converter.convert_to_u('U2')
    print(converted_moves_three)
    converter.clear_converted_moves()


if __name__ == '__main__':
    main()
"""
