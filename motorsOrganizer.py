from motorController import MotorController
from algConverter import AlgConverter


class MotorsOrganizer:
    def __init__(self) -> None:
        self.algConverter = AlgConverter()
        
        # self.down_controller = MotorController('down')
        # self.front_controller = MotorController('front')
        self.right_controller = MotorController('right')
        # self.back_controller = MotorController('back')
        # self.left_controller = MotorController('left')

    def rotate(self, move: str) -> None:
        if move[0] == 'D':
            # self.down_controller.rotate(move)
            pass

        elif move[0] == 'F':
            pass
            # self.front_controller.rotate(move)

        elif move[0] == 'R':
            self.right_controller.rotate(move)

        elif move[0] == 'B':
            pass
            # self.back_controller.rotate(move)

        elif move[0] == 'L':
            # self.left_controller.rotate(move)
            pass

    def cleanup(self) -> None:
        """GPIO clean up. Also deletes all the objects"""
        
        MotorController.cleanup()
        # del self.down_controller
        # del self.front_controller
        del self.right_controller
        # del self.back_controller
        # del self.left_controller

        del self.algConverter
