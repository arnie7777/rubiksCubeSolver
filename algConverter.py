class AlgConverter:
    def __init__(self) -> None:
        self.map_moves: dict[str, str] = {'U': 'D', 'U\'': 'D\'', 'U2': 'D2'}
        self.converted_moves: list[str] = []

    def convert_to_u(self, move):
        '''Converts the given top/U move to a set of moves
        which reults in the same given move, but without
        moving the top of the cube direcly
        Returns the list of moves'''
        self.__convert_to_u_helper()
        self.converted_moves.append(self.map_moves[move])
        self.__convert_to_u_helper()
        return self.converted_moves

    def __convert_to_u_helper(self) -> None:
        self.converted_moves.extend(['R', 'L', 'F2', 'B2', 'R\'', 'L\''])

    def clear_converted_moves(self) -> None:
        self.converted_moves.clear()
