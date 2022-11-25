from tkinter import *
from guiInputValidator import GuiInputValidator
from guiDataStorer import GuiDataStorer
import tkinter.messagebox


class GuiScrambleCubeFrame:
    def __init__(self, right_frame, guiDataStorer) -> None:
        self.guiInputValidator = GuiInputValidator()
        self.guiDataStorer: GuiDataStorer = guiDataStorer
        self.right_frame = right_frame
        self.__create_scramble_cube_frame()

    def __create_scramble_cube_frame(self):
        # create frame for center color of the cube
        frame = Frame(self.right_frame, bg='orange')
        frame.pack(padx=10, pady=10)
        
        # create top label for the frame
        Label(frame, text=f'Enter scrambled cube').pack()

        # create empty label where the scrabled cube will be displayed
        self.scrambled_cube_label = Label(frame)
        self.scrambled_cube_label.pack()

        Button(frame, text='White', command=lambda: self.__add_color_to_label('W')).pack(side='left')
        Button(frame, text='Yellow', command=lambda: self.__add_color_to_label('Y')).pack(side='left')
        Button(frame, text='Red', command=lambda: self.__add_color_to_label('R')).pack(side='left')
        Button(frame, text='Orange', command=lambda: self.__add_color_to_label('O')).pack(side='left')
        Button(frame, text='Blue', command=lambda: self.__add_color_to_label('B')).pack(side='left')
        Button(frame, text='Green', command=lambda: self.__add_color_to_label('G')).pack(side='left')

        # not supposed to be located in this class.. but it works
        Button(self.right_frame, text='Undo', command=lambda: self.__undo_last_color()).pack()

    def __add_color_to_label(self, color):
        scrambled_cube_so_far: str = self.scrambled_cube_label.cget('text')
        if self.guiInputValidator.scramble_color_is_valid(scrambled_cube_so_far, color):
            self.scrambled_cube_label.config(text = scrambled_cube_so_far + color)
            self.guiDataStorer.set_scrambled_cube_so_far(scrambled_cube_so_far + color)
            return
        tkinter.messagebox.showinfo(title = 'Invalid scramle', message = 'A color can at most occur 9 times')

    def __undo_last_color(self):
        self.scrambled_cube_label.config(text = self.scrambled_cube_label.cget('text')[:-1])