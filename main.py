from gui.guiInitializer import GuiInitializer
from gui.models.cubeSolutionModel import CubeSolutionModel


def main():
    solutionModel: CubeSolutionModel = CubeSolutionModel()
    GuiInitializer(solutionModel)
    solution: list[str] = solutionModel.get_solution()

    print('GUI shut down..')


if __name__ == '__main__':
    main()
