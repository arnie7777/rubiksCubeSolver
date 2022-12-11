from gui.views.centerColorFrame import CenterColorFrame
from gui.views.scrambledCubeFrame import ScrambledCubeFrame
from gui.views.solvingFrame import SolvingFrame


class WidgetToggler:
    def __init__(self, top_color_frame: CenterColorFrame, front_color_frame: CenterColorFrame,
                 right_color_frame: CenterColorFrame, scrambled_cube_frame: ScrambledCubeFrame,
                 solving_frame: SolvingFrame):

        self.top_color_frame: CenterColorFrame = top_color_frame
        self.front_color_frame: CenterColorFrame = front_color_frame
        self.right_color_frame: CenterColorFrame = right_color_frame
        self.scrambled_cube_frame: ScrambledCubeFrame = scrambled_cube_frame
        self.solving_frame: SolvingFrame = solving_frame

        self.dis_or_enable = 'disabled'

    def toggle_widgets_in_frames(self):
        self.top_color_frame.toggle_widgets(self.dis_or_enable)
        self.front_color_frame.toggle_widgets(self.dis_or_enable)
        self.right_color_frame.toggle_widgets(self.dis_or_enable)
        self.scrambled_cube_frame.toggle_widgets(self.dis_or_enable)

        if self.dis_or_enable == 'disabled':
            self.dis_or_enable = 'normal'
            return
        self.dis_or_enable = 'disabled'
