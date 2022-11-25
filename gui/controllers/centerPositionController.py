from gui.models.centerColorModel import CenterColorModel
from gui.views.centerColorFrame import CenterColorFrame


class CenterPositionController:
    def __init__(self, model: CenterColorModel, frame: CenterColorFrame) -> None:
        self.model: CenterColorModel = model
        self.frame: CenterColorFrame = frame

    def color_button_clicked(self, color: str) -> None:
        """Save model and update view/frame to display the chosen color in the label"""
        self.model.set_center_color(color)
        self.frame.update_selected_color(color)
