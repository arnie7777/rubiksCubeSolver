class CubeSolutionModel:
    def __init__(self) -> None:
        self.solution: list[str] = []

    def get_solution(self) -> list[str]:
        """Returns a valid solution as a list of strings"""
        return self.solution

    def set_solution(self, solution: list[str]) -> None:
        """Is used to set a valid solution"""
        self.solution = solution
