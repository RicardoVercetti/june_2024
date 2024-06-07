# py_pad.py
from typing import List

FILE_NAME = "notes_data.txt"

class PyPad():
	def __init__(self):
		self.all_notes: List[dict] = []  # import from files
		self.file_retrived = ""
		self.load_from_file()
		# print("all notes initialized")

	def show_all_notes(self):
		for n in self.all_notes:
			print("="*20)
			# print("type of n: ", type(n))
			print("Title : ", n.get("title"))
			print("Body : ", n.get("body"))
		print("="*20)

	def add_note(self, note: dict):
		self.all_notes.append(note)
		# self.append_in_file(note)
		self.save_all_in_file()
		print("Written into the file!")

	def remove_note(self, title: str):
		for note in self.all_notes:
			if note["title"] == title:
				self.all_notes.remove(note)
				print(f"The note with title {title} removed!")
		self.save_all_in_file()

	def edit_note(self, old_title: str, new_note: dict):
		for index, note in enumerate(self.all_notes):
			if note.get("title") == old_title:
				print("Found the element to edit at index : ", index)
				self.all_notes[index] = new_note
				break
		self.save_all_in_file()

	def load_from_file(self):
		try:
			with open(FILE_NAME, "r") as f:
				print("File found!")
				self.file_retrived = f.readlines()
				for item in self.file_retrived:
					if not len(item) <=1:
						title, body = item.split("||")
						# print("--From retrived--")
						# print("Title : ", title)
						# print("Body : ", body)
						self.all_notes.append(dict(title=title, body=body))
				# print("Data : ", self.file_retrived)
		except FileNotFoundError:
			with open(FILE_NAME, "w") as f:
				f.write("Initialized file")
				print("File initiated")

	# this is not needed
	def append_in_file(self, note: dict):
		with open(FILE_NAME, "a") as f:
			f.write(f"{note.get('title')}||{note.get('body')}")
			f.write("\n")

	def save_all_in_file(self):
		with open(FILE_NAME, "w") as f:   # overwrites all the contects in file along with new value added
			for note in self.all_notes:
				f.write(f"{note.get('title')}||{note.get('body')}")
				f.write("\n")
			print("Written all notes into the file")



def initialization():
	note_one = dict(title="title 1", body="This is a dummy note body 1")
	note_two = dict(title="title 2", body="This is a dummy note body 2")
	pypad = PyPad()
	pypad.add_note(note_one)
	pypad.add_note(note_two)
	# pypad.show_all_notes()
	new_dict = dict(title="title 3 at 2", body="This is a dummy note body 3 overwriting 2")
	pypad.edit_note("title 2", new_dict)
	# pypad.show_all_notes()


if __name__ == "__main__":
	initialization()







# each notes should have a title and content
# dict{str, str}
# so all notes will be a list of this dictionaries
