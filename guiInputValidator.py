from cubeSolver import CubeSolver
from colorSideMapper import ColorSideMapper


class GuiInputValidator:
    def __init__(self) -> None:
        self.cube_solver: CubeSolver = CubeSolver()
        self.colorSideMapper: ColorSideMapper = ColorSideMapper()

    """
    # i think i'm not going to use this method anyway
    def scrambled_cube_is_valid(self, scrambled_cube: str) -> bool:
        solution: list[str] = []
        if len(solution) > 1:
            return True
        return False
    """

    def center_colors_are_valid(top: str, front: str, right: str) -> bool:
        # if we are going to do this check, then I think it's a good idea to use the colorSideMapper object
        pass

    def scramble_color_is_valid(self, scrambled_cube_so_far: str, color: str):
        count_color = 0
        for added_color in scrambled_cube_so_far:
            if added_color == color:
                count_color += 1
        if count_color < 9:
            return True
        return False
