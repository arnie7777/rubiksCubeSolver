from gui.models.scrambledCubeModel import ScrambledCubeModel
import gui.views.scrambledCubeFrame as scf
import gui.models.scrambledCubeModel as scm


class ScrambledCubeController:
    # class attribute with constant value
    max_color_occurrence: int = 9
    
    def __init__(self, model: ScrambledCubeModel, frame) -> None:
        self.model: scm.ScrambledCubeModel = model
        self.frame: scf.ScrambledCubeFrame = frame

    def color_button_clicked(self, color_prefix: str, scrambled_cube_so_far: str) -> None:
        if self.__color_prefix_is_valid(color_prefix, scrambled_cube_so_far):
            scrambled_cube_so_far_update: str = scrambled_cube_so_far + color_prefix
            self.model.set_scrambled_cube_so_far(scrambled_cube_so_far_update)
            self.frame.add_prefix_color_success(scrambled_cube_so_far_update)
            return

        self.frame.add_prefix_color_error(
            f'A color can at most occur {ScrambledCubeController.max_color_occurrence} times')

    def undo_button_clicked(self, scrambled_cube_so_far: str) -> None:
        scrambled_cube_so_far_update: str = scrambled_cube_so_far[:-1]
        self.model.set_scrambled_cube_so_far(scrambled_cube_so_far_update)
        self.frame.remove_last_color_prefix(scrambled_cube_so_far_update)

    def __color_prefix_is_valid(self, color_prefix: str, scrambled_cube_so_far: str) -> bool:
        """Checks if the same color prefix occurs less than 9 times:
        Returns true if less than 9 times. Else returns false"""
        count_color_prefix: int = 0
        for added_color_prefix in scrambled_cube_so_far:
            if added_color_prefix == color_prefix:
                count_color_prefix += 1
        if count_color_prefix < ScrambledCubeController.max_color_occurrence:
            return True

        return False
