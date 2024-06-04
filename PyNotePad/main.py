# main.py
from tkinter import *
from create_elements import *

m = Tk()
m.title("PyNotePad")
m.geometry("600x400")
m.resizable(False, False)

saved = []

temp = ""

def save_to_list(text: str):
	print("Passed text : ", text)
	print("gotta save to playlist") 


def add_note():
	text_area = Text(m, height=10, width=20)
	text_area.grid(row=1, column=0)
	btn = Button(m, text="Save note", height=10, width=20, command=lambda: save_to_list(text_area.text))
	btn.grid(row=1, column=1)
	print("Add button clicked")



# create note
add_button = create_button(m, "Add note", 25, add_note)



m.mainloop()

print("Runs...")



# sample


# cloude AI is some what okay I would say. 
# But a lot of improvement is required to 
# make a best outcome out of it.