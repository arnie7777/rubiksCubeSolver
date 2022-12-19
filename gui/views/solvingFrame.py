import threading
import time
import tkinter as tk
import widgetToggler as wd
import gui.controllers.scrambledCubeController as scc
from threading import *


class SolvingFrame:
    def __init__(self, right_frame: tk.Frame) -> None:
        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame)
        self.frame.pack(pady=5)

        # create top label for the frame for count down solving time
        self.count_down_label: tk.Label = tk.Label(self.frame, font=('Arial', 16))
        self.count_down_label.pack_forget()

        self.actual_solving_time_label: tk.Label = tk.Label(self.frame, font=('Arial', 16))
        self.actual_solving_time_label.pack_forget()

        self.controller: scc.ScrambledCubeController = None
        self.widget_disabler: wd.WidgetToggler = None

    def set_controller(self, controller):
        self.controller = controller

    def set_widget_disabler(self, widget_disabler):
        self.widget_disabler = widget_disabler

    def start_solving_success(self, solving_time: float) -> None:
        #self.widget_disabler.toggle_widgets_in_frames()
        self.actual_solving_time_label.pack_forget()
        self.count_down_label.pack()
        for i in range(round(solving_time), -1, -1):
            self.count_down_label.config(text=f'Solving...\nAbout {i} seconds left')
            time.sleep(1)

    def solving_done(self, solving_time: float):
        #self.widget_disabler.toggle_widgets_in_frames()
        self.count_down_label.pack_forget()
        self.actual_solving_time_label.config(text=f'Cube was solved in {round(solving_time, 2)} seconds')
        self.actual_solving_time_label.pack()

