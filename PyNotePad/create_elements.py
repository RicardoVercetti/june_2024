# create_elements.py
from tkinter import Button, Label, Text, BOTH



def create_button(root, text, width, command):
	button = Button(root, text=text, width=width, command=command)
	button.grid(row=0, column=0, columnspan=2)
	return button

def create_label(root, text):
	label = Label(root, text=text)
	label.pack()
	return label

def create_text(root, width=30, height=40):
	text = Text(root, width=width, height=height)
	text.pack()
	return text


# print("Runs...")