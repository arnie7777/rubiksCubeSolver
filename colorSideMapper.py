class ColorSideMapper:
    def __init__(self) -> None:
        self.opposite_color: dict[str, str] = {'W': 'Y', 'Y': 'W', 'R': 'O', 'O': 'R', 'B': 'G', 'G': 'B'}
        self.opposite_side: dict[str, str] = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L', 'F': 'B', 'B': 'F'}

    def get_opposite_color(self, color: str) -> str:
        """Takes in a color on the cube.
        Returns the opposite color
        """
        return self.opposite_color[color]

    def get_opposite_side(self, side: str) -> str:
        """Takes in a side on the cube.
        Returns the opposite side
        """
        return self.opposite_side[side]