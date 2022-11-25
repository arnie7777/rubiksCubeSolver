import tkinter as tk
import tkinter.messagebox
from gui.controllers.scrambledCubeController import ScrambledCubeController


class ScrambledCubeFrame:
    def __init__(self, right_frame: tk.Frame) -> None:
        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame, bg='orange')
        self.frame.pack(padx=10, pady=10)

        # create top label for the frame
        tk.Label(self.frame, text=f'Enter scrambled cube').pack()

        # create empty label where the scrambled cube will be displayed
        self.scrambled_cube_label = tk.Label(self.frame)
        self.scrambled_cube_label.pack()

        self.__create_button('White', 'W')
        self.__create_button('Yellow', 'Y')
        self.__create_button('Red', 'R')
        self.__create_button('Orange', 'O')
        self.__create_button('Blue', 'B')
        self.__create_button('Green', 'G')

        tk.Button(self.frame, text='Undo', command=lambda: self.controller.undo_button_clicked(
            self.scrambled_cube_label.cget('text'))).pack()

        self.controller: ScrambledCubeController = None

    def set_controller(self, controller: ScrambledCubeController):
        self.controller = controller

    def add_prefix_color_success(self, scrambled_cube_so_far_update: str) -> None:
        """Updated the scrambled cube label if pressed color prefix is valid"""
        self.scrambled_cube_label.config(text=scrambled_cube_so_far_update)

    def add_prefix_color_error(self, error_message: str) -> None:
        """Creates a pop up window with an error message"""
        tkinter.messagebox.showinfo(title='Invalid scramble', message=error_message)

    def remove_last_color_prefix(self, scrambled_cube_so_far_update):
        self.scrambled_cube_label.config(text=scrambled_cube_so_far_update)

    def __create_button(self, color: str, color_prefix: str) -> None:
        tk.Button(self.frame, text=color, command=lambda: self.controller.color_button_clicked(
            color_prefix, self.scrambled_cube_label.cget('text'))).pack(side='left')
