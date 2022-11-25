from tkinter import *
from guiDataStorer import GuiDataStorer
from guiCenterColorFrame import GuiCenterColorFrame
from guiScrambleCubeFrame import GuiScrambleCubeFrame
from cubeSolver import CubeSolver
from algConverter import AlgConverter
import tkinter.messagebox
######from guiInputValidator import GuiInputValidator


class GuiController:
    def __init__(self, guiDataStorer) -> None:
        self.guiDataStorer: GuiDataStorer = guiDataStorer
        self.cube_solver = CubeSolver()
        self.algConverter = AlgConverter()
        #####self.guiInputValidator = GuiInputValidator()

        # create root widget and title
        self.root = Tk()
        self.root.title('Rubiks cube solver')
        
        # create left frame for the center color selection frames
        left_frame = Frame(self.root, bg='black')
        left_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        # create instances of center color frames to put into left frame
        self.top_center_color_frame = GuiCenterColorFrame(left_frame, 'top')
        self.front_center_color_frame = GuiCenterColorFrame(left_frame, 'front')
        self.right_center_color_frame = GuiCenterColorFrame(left_frame, 'right')

        # create right frame for the scrambled cube selection frame
        right_frame = Frame(self.root, bg='gray')
        right_frame.pack(side='left', anchor='nw', expand=True, fill='y')

        self.top_center_color_frame = GuiScrambleCubeFrame(right_frame, guiDataStorer)

        # create button to close window and put it into right frame
        Button(right_frame, text='Done', command=lambda: self.__validate_user_input()).pack(side='bottom')

        self.root.mainloop()

    def __validate_user_input(self):
        scrambled_cube: str = self.guiDataStorer.get_scrambled_cube_so_far()
        if len(scrambled_cube) < 54:  # if scrambled cube is invalid (too short)
            self.__create_messagebox('Scrambled cube must be of length 54')
            return

        # map colors to sides (e.g. if white is top color then W should be mapped to U)
        self.top_center_color_frame.get_selected_color()

        solution: list[str] = self.cube_solver.solve(scrambled_cube)
        if len(solution) < 1:  # if scrambled cube is invalid
            self.__create_messagebox('Not a valid scramble')
            return

        # if scramble is valid (i.e. we have gotten a solution from the cube solver)
        self.guiDataStorer.set_solution(solution)
        self.root.destroy()

    def __create_messagebox(self, error_message: str):
        tkinter.messagebox.showinfo(title='Error occurred', message=error_message)