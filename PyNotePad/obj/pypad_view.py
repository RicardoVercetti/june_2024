# pypad_view.py
from tkinter import *
from tkinter.ttk import *



class PyPadView():
	def __init__(self):
		self.win = Tk()
		self.win.title("PyPad")
		self.win.geometry("600x500")
		self.win.resizable(False, False)
		self.main_screen_buttons = ["Create New", "Show Existing", "load Note"]
		self.main_screen_widgets = []
		self.current_screen = None

	def main_screen(self):
		self.current_screen = "main_screen"
		for i,w in enumerate(self.main_screen_buttons):
			btn = Button(self.win, text=w, command=lambda w=w: self.button_actions(w))  # captures the value and has it as a default value
			btn.grid(row=0, column=i, sticky="nsew")
			self.main_screen_widgets.append(btn)

	def create_note_screen(self):
		self.current_screen = "create_screen"
		print("Create screen loaded")
		# rest of the code

	def start(self):
		self.win.mainloop()

	def button_actions(self, action:str):
		print("Button pressed : ", action)
		if action == self.main_screen_buttons[0]:
			# create new note
			self.clear_screen()
			self.create_note_screen()

	def clear_screen(self):
		if self.current_screen == "main_screen":
			for widget in self.main_screen_widgets:
				widget.grid_forget()


def test():
	ppv = PyPadView()
	ppv.main_screen()
	# ppv.clear_screen()
	ppv.start()


if __name__ == "__main__":
	test()