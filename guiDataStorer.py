class GuiDataStorer:
    def __init__(self) -> None:
        self.top_center_color: str = ''
        self.front_center_color: str = ''
        self.right_center_color: str = ''
        self.scrambled_cube: str = ''
        self.solution: list[str] = []

    def get_top_center_color(self):
        return self.top_center_color

    def set_top_center_color(self, color: str):
        self.top_center_color = color

    def get_front_center_color(self):
        return self.front_center_color

    def set_front_center_color(self, color: str):
        self.front_center_color = color

    def get_right_center_color(self):
        return self.right_center_color

    def set_right_center_color(self, color: str):
        self.right_center_color = color

    def get_scrambled_cube_so_far(self):
        return self.scrambled_cube

    def set_scrambled_cube_so_far(self, scrambled_cube: str):
        self.scrambled_cube = scrambled_cube
    
    def get_solution(self):
        return self.solution

    def set_solution(self, solution):
        self.solution = solution