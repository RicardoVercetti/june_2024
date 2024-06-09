# frames_tkinter.py
from tkinter import *


w = Tk()
w.title("Frames example")
w.geometry("500x400")
w.resizable(False, False)

f = Frame(w)
f.grid(row=0, column=0, padx=10, pady=10,columnspan=3 , sticky="nsew")

create_btn = Button(w, text="Create New Note")
create_btn.grid(row=0, column=0, sticky="nsew")

open_btn = Button(w, text="Open existing Note")
open_btn.grid(row=0, column=1, sticky="nsew")

load_btn = Button(w, text="Load Note")
load_btn.grid(row=0, column=2, sticky="nsew")


# f.grid_rowconfigure(0, weight=1)
# f.grid_rowconfigure(1, weight=1)
# f.grid_columnconfigure(0, weight=1)
# f.grid_columnconfigure(1, weight=1)
# f.grid_columnconfigure(2, weight=1)

# w.grid_rowconfigure(0, weight=1)
# w.grid_columnconfigure(0, weight=1)
f.grid_rowconfigure(0, weight=1)
f.grid_rowconfigure(1, weight=1)
f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(1, weight=1)



# Configure the root window's grid to expand
w.grid_rowconfigure(0, weight=0)  # Do not expand the row with buttons
w.grid_rowconfigure(1, weight=1)
w.grid_columnconfigure(0, weight=1)
w.grid_columnconfigure(1, weight=1)
w.grid_columnconfigure(2, weight=1)


w.mainloop()
print("runs...")