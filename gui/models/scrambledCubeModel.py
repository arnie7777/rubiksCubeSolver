class ScrambledCubeModel:
    def __init__(self) -> None:
        self.scrambled_cube = ''

    def get_scrambled_cube_so_far(self) -> str:
        return self.scrambled_cube

    def set_scrambled_cube_so_far(self, scrambled_cube: str) -> None:
        self.scrambled_cube = scrambled_cube

    def get_length(self):
        return len(self.scrambled_cube)
