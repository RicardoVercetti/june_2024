# py_pad.py
from typing import List
# import logging

FILE_NAME = "notes_data.txt"

class PyPad():
	def __init__(self):
		self.all_notes: List[dict] = []  # import from files
		self.load_from_file()
		# print("all notes initialized")

	def show_all_notes(self) -> None:
		for n in self.all_notes:
			print("="*20)
			# print("type of n: ", type(n))
			print("Title : ", n.get("title"))
			print("Body : ", n.get("body"))
		print("="*20)

	def get_all_notes(self) -> List[dict]:
		return self.all_notes

	def add_note(self, note: dict) -> None:
		self.all_notes.append(note)
		self.save_all_in_file()
		# print("Written into the file!")

	def remove_note(self, title: str) -> None:
		for note in self.all_notes:
			if note["title"] == title:
				self.all_notes.remove(note)
				print(f"The note with title {title} removed!")
				break             # fist found note with the title is removed
		self.save_all_in_file()

	def edit_note(self, old_title: str, new_note: dict) -> None:
		for index, note in enumerate(self.all_notes):
			if note.get("title") == old_title:
				print("Found the element to edit at index : ", index)
				self.all_notes[index] = new_note
				print([x for x in self.all_notes])
				break
		self.save_all_in_file()

	# load the default file, if there isn't, create one
	def load_from_file(self) -> None:
		try:
			with open(FILE_NAME, "r") as f:
				print("File found!")
				notes = f.readlines()
				data_from_file_retrived = [note.strip() for note in notes if note.strip()] # otherwise reading auto adds \n
				# print(data_from_file_retrived)
				for item in data_from_file_retrived:
					if not len(item) <=1:
						# print("Item found = ",item)
						title, body = item.split("||")
						# print("--From retrived--")
						# print("Title : ", title)
						# print("Body : ", body)
						self.all_notes.append(dict(title=title, body=body))
				# print("Data : ", data_from_file_retrived)
		except FileNotFoundError:
			with open(FILE_NAME, "w") as f:
				# f.write("Initialized file")
				print("File initiated")

	def save_all_in_file(self) -> None:
		with open(FILE_NAME, "w") as f:   # overwrites all the contects in file along with new value added
			for note in self.all_notes:
				f.write(f"{note.get('title')}||{note.get('body')}\n")
				# f.write("\n")
			print("Written all notes into the file")
		# load_n_show_from_file()


def load_n_show_from_file() -> None:
    with open(FILE_NAME, "r") as f:
        notes = f.readlines()
        notes = [note.strip() for note in notes if note.strip()]
    print("Loaded and shown from file:", notes)


def initialization():
	note_one = dict(title="title 1", body="This is a dummy note body 1")
	note_two = dict(title="title 2", body="This is a dummy note body 2")
	pypad = PyPad()
	# pypad.add_note(note_one)
	# pypad.add_note(note_two)
	# pypad.show_all_notes()
	# new_dict = dict(title="title 3 at 2", body="This is a dummy note body 3 overwriting 2")
	# pypad.edit_note("title 2", new_dict)
	pypad.show_all_notes()


if __name__ == "__main__":
	initialization()







# each notes should have a title and content
# dict{str, str}
# so all notes will be a list of this dictionaries
