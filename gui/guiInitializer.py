import tkinter as tk
from gui.models.cubeSolutionModel import CubeSolutionModel
from gui.models.centerColorModel import CenterColorModel
from gui.controllers.centerPositionController import CenterPositionController
from gui.views.centerColorFrame import CenterColorFrame
from gui.models.scrambledCubeModel import ScrambledCubeModel
from gui.views.scrambledCubeFrame import ScrambledCubeFrame
from gui.controllers.scrambledCubeController import ScrambledCubeController


class GuiInitializer:
    def __init__(self, cubeSolution: CubeSolutionModel) -> None:
        # create window/root widget
        window = tk.Tk()
        window.title('Rubik\'s cube solver')

        # create models
        top_center_color_model: CenterColorModel = CenterColorModel()
        front_center_color_model: CenterColorModel = CenterColorModel()
        right_center_color_model: CenterColorModel = CenterColorModel()
        scrambled_cube_model: ScrambledCubeModel = ScrambledCubeModel()
        self.cubeSolution = cubeSolution  # model which will be used after gui has been shut down

        # create frames/views
        # create left frame for the center color selection frames
        left_frame = tk.Frame(window, bg='black')
        left_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        # create instances of center color frames to put into left frame
        top_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "top")
        front_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "front")
        right_center_color_frame: CenterColorFrame = CenterColorFrame(left_frame, "right")

        # create right frame for the scrambled cube selection frame
        right_frame = tk.Frame(window, bg='gray')
        right_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        # create scrambled cube frame to put into right frame
        scrambled_cube_frame: ScrambledCubeFrame = ScrambledCubeFrame(right_frame)

        # create controllers
        top_center_position_controller = CenterPositionController(top_center_color_model, top_center_color_frame)
        front_center_position_controller = CenterPositionController(front_center_color_model, front_center_color_frame)
        right_center_position_controller = CenterPositionController(right_center_color_model, right_center_color_frame)
        scrambled_cube_controller = ScrambledCubeController(scrambled_cube_model, scrambled_cube_frame)

        # set controllers in the frame/views objects
        top_center_color_frame.set_controller(top_center_position_controller)
        front_center_color_frame.set_controller(front_center_position_controller)
        right_center_color_frame.set_controller(right_center_position_controller)
        scrambled_cube_frame.set_controller(scrambled_cube_controller)

        window.mainloop()