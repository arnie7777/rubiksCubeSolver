from gui import GUI
from guiInputStorer import GuiInputStorer

guiInputStorer = GuiInputStorer()
gui = GUI(guiInputStorer)

del gui
a = guiInputStorer.get_top_center_color()

print(a)