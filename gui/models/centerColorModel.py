class CenterColorModel:
    def __init__(self) -> None:
        self.center_color: str = ''

    def get_center_color(self) -> str:
        """Returns center color"""
        return self.center_color

    def set_center_color(self, center_color: str) -> None:
        """Sets center color"""
        self.center_color = center_color
