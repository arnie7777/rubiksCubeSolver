import time

from gui.models.scrambledCubeModel import ScrambledCubeModel
from gui.models.cubeSolutionModel import CubeSolutionModel
from gui.models.centerColorsModel import CenterColorsModel
from colorSideMapper import ColorSideMapper
from algConverter import AlgConverter
from centerColorsValidator import CenterColorsValidator
from cubeSolver import CubeSolver
from gui.views.solvingFrame import SolvingFrame
from motorsOrganizer import MotorsOrganizer
import gui.views.scrambledCubeFrame as scf
import gui.models.scrambledCubeModel as scm
from threading import *
from timer import Timer


class ScrambledCubeController:
    # class attributes with constant value
    max_color_occurrence: int = 9
    scrambled_cube_len_requirement: int = 54

    def __init__(self, scrambled_cube_model: ScrambledCubeModel, center_colors_model: CenterColorsModel,
                 scrambled_cube_frame, solving_frame: SolvingFrame, window) -> None:
        self.widow = window

        self.scrambled_cube_model: scm.ScrambledCubeModel = scrambled_cube_model
        self.center_colors_model: CenterColorsModel = center_colors_model
        self.scrambled_cube_frame: scf.ScrambledCubeFrame = scrambled_cube_frame

        self.center_colors_validator: CenterColorsValidator = CenterColorsValidator()
        self.color_side_mapper: ColorSideMapper = ColorSideMapper()
        self.cube_solver = CubeSolver()
        self.solutionModel: CubeSolutionModel = CubeSolutionModel()

        self.solving_frame: SolvingFrame = solving_frame

        self.solution_without_u: list[str] = []

    def color_button_clicked(self, color_letter: str, color, scrambled_cube_so_far: str) -> None:
        if self.__color_is_valid(color_letter, scrambled_cube_so_far):
            scrambled_cube_so_far_update: str = scrambled_cube_so_far + color_letter
            length_of_scrambled_cube: int = self.__len_of_scrambled_colors_so_far(scrambled_cube_so_far_update)
            if length_of_scrambled_cube % 9 == 0 and length_of_scrambled_cube < 54:
                scrambled_cube_so_far_update += '\n'
            self.scrambled_cube_model.set_scrambled_cube_so_far(scrambled_cube_so_far_update)
            self.scrambled_cube_frame.add_color_success(scrambled_cube_so_far_update)
            return

        self.scrambled_cube_frame.add_color_error(
            f'A color can at most occur {ScrambledCubeController.max_color_occurrence} times')

    def undo_button_clicked(self, scrambled_cube_so_far: str) -> None:
        print("The width of Tkinter window:", self.widow.winfo_width())
        print("The height of Tkinter window:", self.widow.winfo_height())
        if len(scrambled_cube_so_far) == 0:
            return
        scrambled_cube_so_far_update: str = scrambled_cube_so_far[:-1]
        if scrambled_cube_so_far[-1] == '\n':
            scrambled_cube_so_far_update = scrambled_cube_so_far[:-2]
        self.scrambled_cube_model.set_scrambled_cube_so_far(scrambled_cube_so_far_update)
        self.scrambled_cube_frame.remove_last_color(scrambled_cube_so_far_update)

    def clear_button_clicked(self):
        self.scrambled_cube_frame.clear_scramble('')

    def start_solving_button_clicked(self):
        # if center colors are invalid
        if not self.__center_colors_are_valid():
            self.scrambled_cube_frame.start_solving_error('Make sure the center colors are correct selected')
            return

        # if scrambled cube is invalid (too short)
        if self.scrambled_cube_model.get_length() < ScrambledCubeController.scrambled_cube_len_requirement:
            self.scrambled_cube_frame.start_solving_error(
                f'Scrambled cube must be of length {ScrambledCubeController.scrambled_cube_len_requirement}')
            return

        # configure mapping from the chosen center colors selected by the user
        self.__configure_color_side_mapping()

        # map colors to side, because kociemba library does not accept colors. E.g. if user chooses top color to
        # be W (white) then w will be mapped to U (up) and Y (yellow) will be mapped to D (down)
        scrambled_cube: str = ''
        scrambled_cube_color: str = self.scrambled_cube_model.get_scrambled_cube_so_far()
        for color in scrambled_cube_color:
            scrambled_cube += self.color_side_mapper.map_to_side(color)

        # Change order to what the kociemba library accepts (which is U, R, F, D, L, B)
        # Order entered by the user is U, D, F, R, B, L
        # This is simply done because it's easier for the user to enter this order rather than the
        # kociemba library order
        scrambled_cube = \
            scrambled_cube[0:9] + \
            scrambled_cube[27:36] + \
            scrambled_cube[18:27] + \
            scrambled_cube[9:18] + \
            scrambled_cube[45:54] + \
            scrambled_cube[36:45]

        solution: list[str] = self.cube_solver.solve(scrambled_cube)
        # Try using the solver, to see if the scrambled cube is solvable
        if solution[0] == '':  # If scrambled cube is not solvable
            self.scrambled_cube_frame.start_solving_error('Not a valid scramble.')
            return

        # We must do this because the kociemba library comes up with an algorithm
        # which ends up with an solution, which doesn't make sense, when the cube is already solved.
        if self.__cube_is_already_solved(scrambled_cube):
            self.scrambled_cube_frame.start_solving_error('Cube is already solved')
            return
        
        # Code reaches here if scramble is valid (i.e. we have gotten a solution from the cube solver)
        self.solutionModel.set_solution(solution)
        solution: list[str] = self.solutionModel.get_solution()

        # Create converter object to convert U moves such that top of the cube will not be moved
        alg_converter: AlgConverter = AlgConverter()
        self.solution_without_u.clear()

        # map solution to new solution to get rid of U (up)
        for move in solution:
            if move[0] != 'U':
                self.solution_without_u.append(move)
                continue
            self.solution_without_u.extend(alg_converter.convert_to_u(move))
            alg_converter.clear_converted_moves()

        estimated_time: float = 0
        for move in self.solution_without_u:
            if move[-1] == '2':
                estimated_time += 2.15
                continue
            estimated_time += 1.075

        # create new thread to update view with estimated time remaining
        t1 = Thread(target=lambda: self.solving_frame.start_solving_success(estimated_time))
        t1.start()

        t2 = Thread(target=lambda: self.__start_motors(estimated_time))
        t2.start()

    def __start_motors(self, test):
        solving_timer: Timer = Timer()
        solving_timer.start()

        print(self.solution_without_u)
        
        motor_organizer = MotorsOrganizer()

        for move in self.solution_without_u:
            motor_organizer.rotate(move)

        motor_organizer.cleanup()
        del motor_organizer
        
        

        solving_time = solving_timer.stop()
        self.solving_frame.solving_done(solving_time)

    def __color_is_valid(self, color: str, scrambled_cube_so_far: str) -> bool:
        """Checks if the same color occurs less than 9 times:
        Returns true if less than 9 times. Else returns false"""
        count_color: int = 0
        for added_color in scrambled_cube_so_far:
            if added_color == color:
                count_color += 1
        if count_color < ScrambledCubeController.max_color_occurrence:
            return True

        return False

    def __configure_color_side_mapping(self) -> None:
        top_color: str = self.center_colors_model.get_top_color_model().get_center_color()
        front_color: str = self.center_colors_model.get_front_color_model().get_center_color()
        right_color: str = self.center_colors_model.get_right_color_model().get_center_color()

        self.color_side_mapper.configure_top_front_right_map(top_color, front_color, right_color)

    def __center_colors_are_valid(self) -> bool:
        return self.center_colors_validator.center_colors_are_valid(
            self.center_colors_model.get_top_color_model().get_center_color(),
            self.center_colors_model.get_front_color_model().get_center_color(),
            self.center_colors_model.get_right_color_model().get_center_color())

    def __cube_is_already_solved(self, scrambled_cube) -> bool:
        cube_is_already_solved = True
        colors_appeared = []
        for i in range(1, len(scrambled_cube) - 1):
            current_color = scrambled_cube[i]
            previous_color = scrambled_cube[i-1]
            if previous_color != current_color:
                if previous_color in colors_appeared:
                    cube_is_already_solved = False
                    break
                colors_appeared.append(previous_color)

        return cube_is_already_solved

    def __len_of_scrambled_colors_so_far(self, scrambled_cube_so_far):
        count: int = 0
        for char in scrambled_cube_so_far:
            if char != '\n':
                count += 1
        return count
