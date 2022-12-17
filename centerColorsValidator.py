class CenterColorsValidator:
    def __init__(self):
        self.all_combinations: list[tuple[str:str]] = []

        white_top_possibilities: list[str] = ['R', 'B', 'O', 'G']
        self.__configure_combinations(white_top_possibilities, 'W')

        yellow_top_possibilities: list[str] = ['R', 'G', 'O', 'B']
        self.__configure_combinations(yellow_top_possibilities, 'Y')

        red_top_possibilities: list[str] = ['W', 'G', 'Y', 'B']
        self.__configure_combinations(red_top_possibilities, 'R')

        orange_top_possibilities: list[str] = ['W', 'B', 'Y', 'G']
        self.__configure_combinations(orange_top_possibilities, 'O')

        blue_top_possibilities: list[str] = ['W', 'R', 'Y', 'O']
        self.__configure_combinations(blue_top_possibilities, 'B')

        green_top_possibilities: list[str] = ['W', 'O', 'Y', 'R']
        self.__configure_combinations(green_top_possibilities, 'G')

    def center_colors_are_valid(self, top: str, front: str, right: str):
        if tuple((top, front, right)) in self.all_combinations:
            return True
        return False

    def __configure_combinations(self, possibilities: list[str], top: str):
        for i in range(4):
            front: str = possibilities[i]
            if i == 3:
                right = possibilities[0]
            else:
                right: str = possibilities[i + 1]
            self.all_combinations.append(tuple((top, front, right)))
