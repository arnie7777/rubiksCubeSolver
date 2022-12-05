from gui.guiInitializer import GuiInitializer
from gui.models.cubeSolutionModel import CubeSolutionModel


def main():
    solutionModel: CubeSolutionModel = CubeSolutionModel()
    GuiInitializer(solutionModel)
    solution: list[str] = solutionModel.get_solution()

    # If user exit window without the 'start solving' button
    if len(solution) == 0:
        exit()

    # If code reaches here it means we have a solution
    # todo turn of touch screen
    # todo loop through solution and use motorOrganizer


if __name__ == '__main__':
    main()
