import tkinter as tk
from colorStorer import ColorStorer
import gui.controllers.centerPositionController as cpc


class CenterColorFrame:
    def __init__(self, left_frame: tk.Frame, center_position: str) -> None:
        # create frame for center color of the cube (use left_frame as parent frame)
        self.frame = tk.Frame(left_frame)
        self.frame.pack(padx=1, pady=1)
        if center_position == 'front':
            self.frame.pack(padx=1, pady=39)

        # create top label for the frame
        tk.Label(self.frame, font=('Arial', 8), text=f'Enter {center_position} center color of the cube').pack()

        # create empty label where the chosen color by the user will be displayed
        self.selected_color_label = tk.Label(self.frame, font=('Arial', 8))
        self.selected_color_label.pack()

        self.__create_button('White', ColorStorer.get_white())
        self.__create_button('Yellow', ColorStorer.get_yellow())
        self.__create_button('Red', ColorStorer.get_red())
        self.__create_button('Orange', ColorStorer.get_orange())
        self.__create_button('Blue', ColorStorer.get_blue())
        self.__create_button('Green', ColorStorer.get_green())

        self.controller: cpc.CenterPositionController = None

    def set_controller(self, controller) -> None:
        """Sets the controller to take care of events from this view/frame"""
        self.controller = controller

    def update_selected_color(self, color_text: str, color: str) -> None:
        """Updates the label to display the selected color"""
        self.selected_color_label.config(text=color_text, bg=color)

    def __create_button(self, color_text: str, color: str) -> None:
        tk.Button(self.frame, text=color_text, bg=color, width='3', font=('Arial', 8),
                  command=lambda: self.controller.color_button_clicked(color_text, color)).pack(side='left')

    def toggle_widgets(self, dis_or_enable: str):
        for child in self.frame.winfo_children():
            child.configure(state=dis_or_enable)
