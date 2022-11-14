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

    """
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
    """

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
