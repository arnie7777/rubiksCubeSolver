from tkinter import *

class GUI:
    def __init__(self) -> None:
        self.__start_screen_setup()
        

    def __start_screen_setup(self):
        self.root = Tk()
        self.root.title('Rubiks cube solver')

        self.top_color_frame = Frame(self.root).grid(row=0, column=0)
        
        self.top_color_label = Label(self.top_color_frame, text='Enter top center color of the cube')
        self.top_color_label.grid(row=0, column=0, columnspan=7)

        self.top_color_entry = Label(self.top_color_frame)
        self.top_color_entry.grid(row=1, column=0, columnspan=7)

        Button(self.top_color_frame, text='White', command=lambda: self.__top_color_entered('White')).grid(row=2, column=0)
        Button(self.top_color_frame, text='Yellow', command=lambda: self.__top_color_entered('Yellow')).grid(row=2, column=1)
        Button(self.top_color_frame, text='Red', command=lambda: self.__top_color_entered('Red')).grid(row=2, column=4)
        Button(self.top_color_frame, text='Orange', command=lambda: self.__top_color_entered('Orange')).grid(row=2, column=5)
        Button(self.top_color_frame, text='Blue', command=lambda: self.__top_color_entered('Blue')).grid(row=2, column=2)
        Button(self.top_color_frame, text='Green', command=lambda: self.__top_color_entered('Green')).grid(row=2, column=3)

        self.top_color_frame = Frame(self.root).grid(row=0, column=0)
        
        self.root.mainloop()


    def __top_color_entered(self, color: str):
        self.top_color_entry.config(text=color)

