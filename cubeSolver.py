import kociemba

class CubeSolver():
    def solve(self, cube: str):
        '''Uses a library to get a solution for the cude.
        Returns the result as a list of strings'''
        solution_as_string = kociemba.solve(cube)
        return list(solution_as_string.split(' '))
