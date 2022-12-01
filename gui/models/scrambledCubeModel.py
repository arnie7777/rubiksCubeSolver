class ScrambledCubeModel:
    def __init__(self) -> None:
        self.scrambled_cube = ''

    def get_scrambled_cube_so_far(self) -> str:
        scrambled_cube_no_new_lines: str = ''
        for char in self.scrambled_cube:
            if char != '\n':
                scrambled_cube_no_new_lines += char
        return scrambled_cube_no_new_lines

    def set_scrambled_cube_so_far(self, scrambled_cube: str) -> None:
        self.scrambled_cube = scrambled_cube

    def get_length(self):
        count: int = 0
        for char in self.scrambled_cube:
            if char != '\n':
                count += 1
        return count
