import tkinter as tk
import tkinter.messagebox
from gui.controllers.scrambledCubeController import ScrambledCubeController


class ScrambledCubeFrame:
    def __init__(self, right_frame: tk.Frame) -> None:
        self.right_frame = right_frame

        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame, bg='orange')
        self.frame.pack(padx=10, pady=10)

        # create top label for the frame
        tk.Label(self.frame, text=f'Enter cube (order: U, D, F, R, B, L)').pack()
        # short 'YWYYWYYWY\nWYWWYWWYW\nOROOROORO\nBBBBBBBBB\nRORRORROR\nGGGGGGGGG'
        # long 'WWWWWWWWW\nYYYYYYYYY\nGGGRRRRRR\nRRRBBBBBB\nBBBOOOOOO\nOOOGGGGGG'
        # create empty label where the scrambled cube will be displayed
        self.scrambled_cube_label = tk.Label(self.frame, text='YWYYWYYWY\nWYWWYWWYW\nOROOROORO\nBBBBBBBBB\nRORRORROR\nGGGGGGGGG')
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

    def test(self, i):
        self.scrambled_cube_label.config(text=f'{i}')

    def start_solving_error(self, error_message: str) -> None:
        self.__create_messagebox(error_message)

    def start_solving_success(self) -> None:
        """Displays information about the solution"""
        # todo display the following:
        # solving time
        # number of moves
        # maybe the solution
        # maybe clear all fields
        pass

    def __create_button(self, color: str) -> None:
        tk.Button(self.frame, text=color, command=lambda: self.controller.color_button_clicked(
            color[0], self.scrambled_cube_label.cget('text'))).pack(side='left')

    def __create_messagebox(self, error_message: str):
        tkinter.messagebox.showinfo(title='Error occurred', message=error_message)

    def toggle_widgets(self, dis_or_enable: str):
        for child in self.frame.winfo_children():
            child.configure(state=dis_or_enable)

        for child in self.right_frame.winfo_children():
            if child.widgetName == 'frame':
                continue
            child.configure(state=dis_or_enable)

