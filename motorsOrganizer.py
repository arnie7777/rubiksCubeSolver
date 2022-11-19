from motorController import MotorController
from algConverter import AlgConverter

class MotorsOrganizer:
    def __init__(self) -> None:
        self.algConverter = AlgConverter()
        #self.down_controller = MotorController('down')
        #self.front_controller = MotorController('front')
        self.right_controller = MotorController('right')
        #self.back_controller = MotorController('back')
        #self.left_controller = MotorController('left')


    def rotate(self, move: str) -> None:
        '''If move is starts with 'U', then uses alg converter to convert the moves to be executed.
        Else just call execute_rotation directly with the same argument'''
        
        """
        if move[0] == 'U':
            converted_moves: list[str] = self.algConverter.convert_to_u(move)
            for converted_move in converted_moves:
                self.__execute_rotation(converted_move)
            self.algConverter.clear_converted_moves()
            return
        """

        self.__execute_rotation(move)


    def __execute_rotation(self, move: str) -> None:
        '''Makes the final call to the motorController, which takes care of rotating the motor'''
        
        if move[0] == 'D':
            pass
            #self.down_controller.rotate(move)

        elif move[0] == 'F':
            pass
            #self.front_controller.rotate(move)

        elif move[0] == 'R':
            self.right_controller.rotate(move)

        elif move[0] == 'B':
            pass
            #self.back_controller.rotate(move)

        elif move[0] == 'L':
            pass
            #self.left_controller.rotate(move)
    

    def cleanup(self) -> None:
        '''Cleans up all pins on all motors and finally GPIO clean up
        Alse deletes all the objects'''
        
        #self.down_controller.cleanup_pins()
        #self.front_controller.cleanup_pins()
        self.right_controller.cleanup_pins()
        #self.back_controller.cleanup_pins()
        #self.left_controller.cleanup_pins()
        MotorController.cleanup()
        #del self.down_controller
        #del self.front_controller
        del self.right_controller
        #del self.back_controller
        #del self.left_controller

        del self.algConverter