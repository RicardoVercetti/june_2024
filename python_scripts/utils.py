# utils.py

def save_in_a_file(content: str, location: str):
	with open(location, "w", encoding='utf-8') as f:
		f.write(content)

	print("Saved into the file")


def load_from_the_file(file: str) -> str:
	with open(file, "r", encoding="utf-8") as f:
		data = f.read()
		return data

