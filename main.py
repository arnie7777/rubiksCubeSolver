from gui.guiInitializer import GuiInitializer
from gpioController import GpioController
from ledController import LedController


def main():
    GpioController.set_mode()
    # LedController.turn_on_green()

    GuiInitializer()

    # LedController.turn_off_green()
    GpioController.cleanup()


if __name__ == '__main__':
    main()
