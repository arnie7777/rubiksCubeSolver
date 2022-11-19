from motorController import MotorController

def main():
    right_controller = MotorController('right')
    right_controller.rotate('R2')
    right_controller.cleanup()
    

if __name__ == '__main__':
    main()
