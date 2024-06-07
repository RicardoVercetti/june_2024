# file_writing.py


def create_and_write_file():
	with open("sample_file.txt", "r") as f:
		lines = f.read()
		print(lines)



def main():
	create_and_write_file()
	# print("Main ran...")



if __name__ == "__main__":
	main()


