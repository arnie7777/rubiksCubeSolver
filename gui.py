from tkinter import *

class GUI:
    def __init__(self) -> None:
        self.__start_screen_setup()
        

    def __start_screen_setup(self):
        # create root widget and title
        self.root = Tk()
        self.root.title('Rubiks cube solver')

        # create a frame in root
        self.top_color_frame = Frame(self.root).pack(padx=10, pady=10, side='bottom')
        
        # create top label in the frame
        self.top_color_label = Label(self.top_color_frame, text='Enter top center color of the cube').pack()

        # create empty label where the chosen color by the user will be displayed
        self.top_color_entry = Label(self.top_color_frame)
        self.top_color_entry.pack()

        Button(self.top_color_frame, text='White', command=lambda: self.__top_color_entered('White')).pack()
        Button(self.top_color_frame, text='Yellow', command=lambda: self.__top_color_entered('Yellow')).pack()
        Button(self.top_color_frame, text='Red', command=lambda: self.__top_color_entered('Red')).pack()
        Button(self.top_color_frame, text='Orange', command=lambda: self.__top_color_entered('Orange')).pack()
        Button(self.top_color_frame, text='Blue', command=lambda: self.__top_color_entered('Blue')).pack()
        Button(self.top_color_frame, text='Green', command=lambda: self.__top_color_entered('Green')).pack()

        self.top_color_frame = Frame(self.root).pack()

        self.root.mainloop()


    def __top_color_entered(self, color: str):
        self.top_color_entry.config(text=color)

