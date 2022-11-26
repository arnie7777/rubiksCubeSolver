import tkinter as tk
import tkinter.messagebox
from gui.controllers.scrambledCubeController import ScrambledCubeController


class ScrambledCubeFrame:
    def __init__(self, right_frame: tk.Frame, window: tk.Tk) -> None:
        self.window = window

        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame, bg='orange')
        self.frame.pack(padx=10, pady=10)

        # create top label for the frame
        tk.Label(self.frame, text=f'Enter scrambled cube').pack()

        # create empty label where the scrambled cube will be displayed
        self.scrambled_cube_label = tk.Label(self.frame)
        self.scrambled_cube_label.pack()

        self.__create_button('White')
        self.__create_button('Yellow')
        self.__create_button('Red')
        self.__create_button('Orange')
        self.__create_button('Blue')
        self.__create_button('Green')

        # put undo and done buttons directly into right_frame
        tk.Button(right_frame, text='Undo', command=lambda: self.controller.undo_button_clicked(
            self.scrambled_cube_label.cget('text'))).pack()

        tk.Button(
            right_frame, text='Start solving', command=lambda: self.controller.start_solving_button_clicked()).pack()

        self.controller: ScrambledCubeController = None

    def set_controller(self, controller: ScrambledCubeController):
        self.controller = controller

    def add_color_success(self, scrambled_cube_so_far_update: str) -> None:
        """Updated the scrambled cube label if pressed color is valid"""
        self.scrambled_cube_label.config(text=scrambled_cube_so_far_update)

    def add_color_error(self, error_message: str) -> None:
        self.__create_messagebox(error_message)

    def remove_last_color(self, scrambled_cube_so_far_update):
        self.scrambled_cube_label.config(text=scrambled_cube_so_far_update)

    def start_solving_error(self, error_message: str) -> None:
        self.__create_messagebox(error_message)

    def start_solving_success(self) -> None:
        self.window.destroy()

    def __create_button(self, color: str) -> None:
        tk.Button(self.frame, text=color, command=lambda: self.controller.color_button_clicked(
            color[0], self.scrambled_cube_label.cget('text'))).pack(side='left')

    def __create_messagebox(self, error_message: str):
        tkinter.messagebox.showinfo(title='Error occurred', message=error_message)
