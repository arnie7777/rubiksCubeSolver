import tkinter as tk
import gui.controllers.centerPositionController as cpc


class CenterColorFrame:
    def __init__(self, left_frame: tk.Frame, center_position: str) -> None:
        # create frame for center color of the cube (use left_frame as parent frame)
        self.frame = tk.Frame(left_frame, bg='orange')
        self.frame.pack(padx=10, pady=10)
        
        # create top label for the frame
        tk.Label(self.frame, text=f'Enter {center_position} center color of the cube').pack()

        # create empty label where the chosen color by the user will be displayed
        self.selected_color_label = tk.Label(self.frame)
        self.selected_color_label.pack()

        self.__create_button('White')
        self.__create_button('Yellow')
        self.__create_button('Red')
        self.__create_button('Orange')
        self.__create_button('Blue')
        self.__create_button('Green')

        self.controller: cpc.CenterPositionController = None

    def set_controller(self, controller) -> None:
        """Sets the controller to take care of events from this view/frame"""
        self.controller = controller

    def update_selected_color(self, color: str) -> None:
        """Updates the label to display the selected color"""
        self.selected_color_label.config(text=color)

    def __create_button(self, color: str) -> None:
        tk.Button(self.frame, text=color, command=lambda: self.controller.color_button_clicked(color)).pack(side='left')
