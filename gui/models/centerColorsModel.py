from gui.models.centerColorModel import CenterColorModel


class CenterColorsModel:
    def __init__(self, top_center_model: CenterColorModel, front_center_model: CenterColorModel,
                 right_center_model: CenterColorModel):
        self.top_center_model = top_center_model
        self.front_center_model = front_center_model
        self.right_center_model = right_center_model

    def get_top_color_model(self) -> CenterColorModel:
        return self.top_center_model

    def get_front_color_model(self) -> CenterColorModel:
        return self.front_center_model

    def get_right_color_model(self) -> CenterColorModel:
        return self.right_center_model
