import tkinter as tk
import tkinter.messagebox
from colorStorer import ColorStorer
from gui.controllers.scrambledCubeController import ScrambledCubeController


class ScrambledCubeFrame:
    def __init__(self, right_frame: tk.Frame) -> None:
        self.right_frame = right_frame

        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame)
        self.frame.pack(padx=1, pady=1)

        # create top label for the frame
        tk.Label(self.frame, font=('Arial', 8), text=f'Enter cube (order: U, D, F, R, B, L)').pack()
        # short solution 'YWYYWYYWY\nWYWWYWWYW\nOROOROORO\nBBBBBBBBB\nRORRORROR\nGGGGGGGGG'
        # long solution 'WWWWWWWWW\nYYYYYYYYY\nGGGRRRRRR\nRRRBBBBBB\nBBBOOOOOO\nOOOGGGGGG'
        # create empty label where the scrambled cube will be displayed
        self.scrambled_cube_label = tk.Label(self.frame, font=('Arial', 8),
                                             text='YWYYWYYWY\nWYWWYWWYW\nOROOROORO\nBBBBBBBBB\nRORRORROR\nGGGGGGGGG')
        self.scrambled_cube_label.pack()

        self.__create_button('White', ColorStorer.get_white())
        self.__create_button('Yellow', ColorStorer.get_yellow())
        self.__create_button('Red', ColorStorer.get_red())
        self.__create_button('Orange', ColorStorer.get_orange())
        self.__create_button('Blue', ColorStorer.get_blue())
        self.__create_button('Green', ColorStorer.get_green())

        # put undo and done buttons directly into right_frame
        tk.Button(right_frame, text='Undo', width='3', font=('Arial', 8),
                  command=lambda: self.controller.undo_button_clicked(
            self.scrambled_cube_label.cget('text'))).pack(pady=2)

        tk.Button(right_frame, text='Clear all', width='5', font=('Arial', 8),
                  command=lambda: self.controller.clear_button_clicked()).pack(pady=2)

        tk.Button(
            right_frame, text='Start solving', width='10', font=('Arial', 8),
            command=lambda: self.controller.start_solving_button_clicked()).pack(pady=2)

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

    def clear_scramble(self, empty_scramble: str):
        self.scrambled_cube_label.config(text=empty_scramble)

    def start_solving_error(self, error_message: str) -> None:
        self.__create_messagebox(error_message)

    def __create_button(self, color_text: str, color: str) -> None:
        btn = tk.Button(self.frame, text=color_text, bg=color, width='3', font=('Arial', 8),
                        command=lambda: self.controller.color_button_clicked(
                            color_text[0], color, self.scrambled_cube_label.cget('text')))
        btn.pack(side='left')

    def __create_messagebox(self, error_message: str):
        tkinter.messagebox.showinfo(title='Error occurred', message=error_message)

    def toggle_widgets(self, dis_or_enable: str):
        for child in self.frame.winfo_children():
            child.configure(state=dis_or_enable)

        for child in self.right_frame.winfo_children():
            if child.widgetName == 'frame':
                continue
            child.configure(state=dis_or_enable)