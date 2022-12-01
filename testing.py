"""
from tkinter import *

master = Tk()

w = Text(master, height=1, borderwidth=0)
w.insert(1.0, "Hello, world!")
w.pack()

w.configure(state="disabled")

# if tkinter is 8.5 or above you'll want the selection background
# to appear like it does when the widget is activated
# comment this out for older versions of Tkinter
w.configure(inactiveselectbackground=w.cget("selectbackground"))

mainloop()
"""



"""
import tkinter as tk

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()
"""