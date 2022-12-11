import gui.models.centerColorModel as ccm
import gui.views.centerColorFrame as ccf


class CenterPositionController:
    def __init__(self, model, frame) -> None:
        self.model: ccm.CenterColorModel = model
        self.frame: ccf.CenterColorFrame = frame

    def color_button_clicked(self, color: str) -> None:
        """Update view/frame to display the chosen color in the label
        and save the color prefix to the model"""
        self.model.set_center_color(color[0])
        self.frame.update_selected_color(color)
