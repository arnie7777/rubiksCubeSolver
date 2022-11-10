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
    solution = solver.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
    print(solution)
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
