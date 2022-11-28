from motorsOrganizer import MotorsOrganizer
import time


def main():
    time.sleep(3)
    motor_organizer = MotorsOrganizer()
    
    motor_organizer.rotate('R\'')
    time.sleep(1)
    motor_organizer.rotate('L')
    time.sleep(1)
    motor_organizer.rotate('F')
    time.sleep(1)
    motor_organizer.rotate('F')
    time.sleep(1)
    motor_organizer.rotate('L')
    time.sleep(1)
    motor_organizer.rotate('R')
    time.sleep(1)
    
    motor_organizer.cleanup()
    del motor_organizer


if __name__ == '__main__':
    main()
