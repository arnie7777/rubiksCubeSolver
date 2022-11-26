from gui.models.centerColorModel import CenterColorModel
from gui.views.centerColorFrame import CenterColorFrame


class CenterPositionController:
    def __init__(self, model: CenterColorModel, frame: CenterColorFrame) -> None:
        self.model: CenterColorModel = model
        self.frame: CenterColorFrame = frame

    def color_button_clicked(self, color: str) -> None:
        """Update view/frame to display the chosen color in the label
        and save the color prefix to the model"""
        self.model.set_center_color(color[0])
        self.frame.update_selected_color(color)
