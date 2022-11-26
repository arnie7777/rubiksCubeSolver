class ColorSideMapper:
    # this class attribute is constant
    opposite_color: dict[str, str] = {'W': 'Y', 'Y': 'W', 'R': 'O', 'O': 'R', 'B': 'G', 'G': 'B'}

    def __init__(self) -> None:
        self.color_to_side_map: dict[str, str] = {}

    def configure_top_front_right_map(self, top_color: str, front_color: str, right_color: str):
        self.color_to_side_map[top_color] = 'U'
        self.color_to_side_map[self.__get_opposite_color(top_color)] = 'D'

        self.color_to_side_map[front_color] = 'F'
        self.color_to_side_map[self.__get_opposite_color(front_color)] = 'B'

        self.color_to_side_map[right_color] = 'R'
        self.color_to_side_map[self.__get_opposite_color(right_color)] = 'L'

    def map_to_side(self, color: str) -> str:
        """Takes in color and returns the side of that color"""
        return self.color_to_side_map[color]

    def __get_opposite_color(self, color: str) -> str:
        """Takes in a color on the cube.
        Returns the opposite color
        """
        return ColorSideMapper.opposite_color[color]
