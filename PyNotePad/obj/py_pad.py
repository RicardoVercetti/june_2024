# py_pad.py
from typing import List


class PyPad():
	def __init__(self):
		self.all_notes: List[dict] = []  # import from files
		print("all notes initialized")

	def show_all_notes(self):
		for n in self.all_notes:
			print("="*20)
			# print("type of n: ", type(n))
			print("Title : ", n.get("title"))
			print("Body : ", n.get("body"))
		print("="*20)

	def add_note(self, note: dict):
		self.all_notes.append(note)

	def remove_note(self, title: str):
		for note in self.all_notes:
			if note["title"] == title:
				self.all_notes.remove(note)
				print(f"The note with title {title} removed!")


	def edit_note(self, old_title: str, new_note: dict):
		for index, note in enumerate(self.all_notes):
			if note.get("title") == old_title:
			    print("Found the element to edit at index : ", index)
			    self.all_notes[index] = new_note
			    break


def initialization():
	note_one = dict(title="title 1", body="This is a dummy note body 1")
	note_two = dict(title="title 2", body="This is a dummy note body 2")
	pypad = PyPad()
	pypad.add_note(note_one)
	pypad.add_note(note_two)
	# pypad.show_all_notes()
	new_dict = dict(title="title 3 at 2", body="This is a dummy note body 3 overwriting 2")
	pypad.edit_note("title 2", new_dict)
	pypad.show_all_notes()




if __name__ == "__main__":
	initialization()







# each notes should have a title and content
# dict{str, str}
# so all notes will be a list of this dictionaries
