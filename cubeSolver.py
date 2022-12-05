import kociemba


class CubeSolver():
    def solve(self, cube: str):
        """Uses kociemba library to get a solution for the cube.
        Returns the result as a list of strings. If no solution is possible -
        i.e. it's an invalid scramble, then return a list of length 1 which only
        includes an empty string"""
        solution_as_string = ''
        try:
            solution_as_string = kociemba.solve(cube)
        except:
            pass
        
        return list(solution_as_string.split(' '))
