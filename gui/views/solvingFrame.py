import threading
import time
import tkinter as tk
import widgetToggler as wd
import gui.controllers.scrambledCubeController as scc
from threading import *


class SolvingFrame:
    def __init__(self, right_frame: tk.Frame) -> None:
        # create frame for scrambled cube
        self.frame = tk.Frame(right_frame, bg='red')
        self.frame.pack(padx=10, pady=10)

        # create top label for the frame for count down solving time
        self.timer_label: tk.Label = tk.Label(self.frame)
        self.timer_label.pack()

        self.controller: scc.ScrambledCubeController = None
        self.widget_disabler: wd.WidgetToggler = None

        hey = 0

    def set_controller(self, controller):
        self.controller = controller

    def set_widget_disabler(self, widget_disabler):
        self.widget_disabler = widget_disabler

    def start_solving_success(self, solving_time: float) -> None:
        # self.widget_disabler.toggle_widgets_in_frames()
        for i in range(round(solving_time), -1, -1):
            time.sleep(1)
            self.timer_label.config(text=f'Solving...\nAbout {i} seconds left')

    def solving_done(self):
        self.widget_disabler.toggle_widgets_in_frames()
