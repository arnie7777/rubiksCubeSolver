from tkinter import *

class GUI:
    def __init__(self, guiInputStorer) -> None:
        self.guiInputStorer: GuiInputStorer = guiInputStorer

        # create root widget and title
        self.root = Tk()
        self.root.title('Rubiks cube solver')
        
        self.__display_center_color_label()

        self.root.mainloop()

        
    def __display_center_color_label(self):
        # create frame for top center color of the cube
        top_color_frame = Frame(self.root, bg='blue')
        top_color_frame.pack(padx=10, pady=10, side='left', anchor='nw')
        
        # create top label for the frame
        top_color_label = Label(top_color_frame, text='Enter top center color of the cube').pack()

        # create empty label where the chosen color by the user will be displayed
        self.top_color_entry = Label(top_color_frame)
        self.top_color_entry.pack()

        Button(top_color_frame, text='White', command=lambda: self.__top_color_selected('White')).pack(side='left')
        Button(top_color_frame, text='Yellow', command=lambda: self.__top_color_selected('Yellow')).pack(side='left')
        Button(top_color_frame, text='Red', command=lambda: self.__top_color_selected('Red')).pack(side='left')
        Button(top_color_frame, text='Orange', command=lambda: self.__top_color_selected('Orange')).pack(side='left')
        Button(top_color_frame, text='Blue', command=lambda: self.__top_color_selected('Blue')).pack(side='left')
        Button(top_color_frame, text='Green', command=lambda: self.__top_color_selected('Green')).pack(side='left')
        Button(top_color_frame, text='Ok', command=self.root.destroy).pack(side='left')


    def __top_color_selected(self, color: str):
        self.top_color_entry.config(text=color)
        self.guiInputStorer.set_top_center_color(color)
