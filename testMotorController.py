from motorController import MotorController

def main():
    right_controller = MotorController('right')
    right_controller.rotate('R2')
    right_controller.cleanup_pins()
    MotorController.cleanup()
    del right_controller


if __name__ == '__main__':
    main()
