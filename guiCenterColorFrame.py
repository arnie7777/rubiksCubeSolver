from tkinter import *


class GuiCenterColorFrame:
    def __init__(self, left_frame, center_position: str) -> None:
        self.left_frame = left_frame
        self.center_position = center_position
        self.selected_color = ''
        
        self.__create_center_color_frame()

        """
        if center_position == 'top':
            self.__create_center_color_frame('orange')
        elif center_position == 'front':
            self.__create_center_color_frame('orange')
        elif center_position == 'right':
            self.__create_center_color_frame('orange')
        """

    def __create_center_color_frame(self):
        # create frame for center color of the cube
        frame = Frame(self.left_frame, bg='orange')
        frame.pack(padx=10, pady=10)
        
        # create top label for the frame
        Label(frame, text = f'Enter {self.center_position} center color of the cube').pack()

        # create empty label where the chosen color by the user will be displayed
        self.selected_color_label = Label(frame)
        self.selected_color_label.pack()

        Button(frame, text='White', command=lambda: self.__color_selected('White')).pack(side='left')
        Button(frame, text='Yellow', command=lambda: self.__color_selected('Yellow')).pack(side='left')
        Button(frame, text='Red', command=lambda: self.__color_selected('Red')).pack(side='left')
        Button(frame, text='Orange', command=lambda: self.__color_selected('Orange')).pack(side='left')
        Button(frame, text='Blue', command=lambda: self.__color_selected('Blue')).pack(side='left')
        Button(frame, text='Green', command=lambda: self.__color_selected('Green')).pack(side='left')

    def __color_selected(self, color):
        self.selected_color = color
        self.selected_color_label.config(text=color)

    def get_selected_color(self) -> str:
        return self.selected_color
