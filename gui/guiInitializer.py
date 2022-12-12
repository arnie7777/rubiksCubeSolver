import tkinter as tk
from widgetToggler import WidgetToggler
from gui.models.centerColorModel import CenterColorModel
from gui.controllers.centerPositionController import CenterPositionController
from gui.views.centerColorFrame import CenterColorFrame
from gui.models.scrambledCubeModel import ScrambledCubeModel
from gui.views.scrambledCubeFrame import ScrambledCubeFrame
from gui.models.centerColorsModel import CenterColorsModel
from gui.controllers.scrambledCubeController import ScrambledCubeController
from gui.views.solvingFrame import SolvingFrame


class GuiInitializer:
    def __init__(self) -> None:
        # create window/root widget
        window = tk.Tk()
        window.geometry('556x267')
        window.title('Rubik\'s cube solver')

        # create models
        top_center_color_model: CenterColorModel = CenterColorModel()
        front_center_color_model: CenterColorModel = CenterColorModel()
        right_center_color_model: CenterColorModel = CenterColorModel()
        center_colors_model: CenterColorsModel = CenterColorsModel(top_center_color_model, front_center_color_model,
                                                                   right_center_color_model)
        scrambled_cube_model: ScrambledCubeModel = ScrambledCubeModel()

        # create frames/views
        # create left frame for the center color selection frames
        left_frame = tk.Frame(window, bg='gray')
        left_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        # create instances of center color frames to put into left frame
        top_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "top")
        front_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "front")
        right_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "right")

        # create right frame for the scrambled cube selection frame
        right_frame = tk.Frame(window, bg='gray')
        right_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        # create scrambled cube frame to put into right frame,
        # also takes in window, because ScrambledCubeFrame is the one that will
        # destroy the window when the solving of the rubik's cube starts
        scrambled_cube_frame: ScrambledCubeFrame = ScrambledCubeFrame(right_frame)

        # create solvingFrame to put into right frame
        solving_frame: SolvingFrame = SolvingFrame(right_frame)
        solving_frame.set_widget_disabler(WidgetToggler(top_center_color_frame, front_center_color_frame,
                                                        right_center_color_frame, scrambled_cube_frame, solving_frame))

        # create controllers
        top_center_position_controller = CenterPositionController(top_center_color_model, top_center_color_frame)
        front_center_position_controller = CenterPositionController(front_center_color_model, front_center_color_frame)
        right_center_position_controller = CenterPositionController(right_center_color_model, right_center_color_frame)
        scrambled_cube_controller = ScrambledCubeController(scrambled_cube_model, center_colors_model,
                                                            scrambled_cube_frame, solving_frame, window)

        # set controllers in the frame/views objects
        top_center_color_frame.set_controller(top_center_position_controller)
        front_center_color_frame.set_controller(front_center_position_controller)
        right_center_color_frame.set_controller(right_center_position_controller)
        scrambled_cube_frame.set_controller(scrambled_cube_controller)
        solving_frame.set_controller(scrambled_cube_controller)

        window.mainloop()
