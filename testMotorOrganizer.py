from motorsOrganizer import MotorsOrganizer
import time

def main():
    time.sleep(3)
    motor_organizer = MotorsOrganizer()
    
    motor_organizer.rotate('R\'')
    time.sleep(0.3)
    motor_organizer.rotate('R')
    time.sleep(0.3)
    motor_organizer.rotate('R\'')
    time.sleep(0.3)
    motor_organizer.rotate('R2')
    
    motor_organizer.cleanup()
    del motor_organizer


if __name__ == '__main__':
    main()