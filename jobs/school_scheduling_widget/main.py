# main.py

# from Subjects import Subjects
import random
import math


# some setting
subjects_list = ["HISTORY", "MATH", "SCIENCE", "PE", "HEALTH", "GUIDANCE", "ELECTIVE", "CTE"]

def random_subject_list():
	return random.sample(subjects, 4)

class Student():
	def __init__(self, name: str, id: int, subjects: list[str] = None, total_subjects_taken = 5):
		self.name = name
		self.id = id
		if subjects == None:
			self.subjects = random.sample(subjects_list, total_subjects_taken)
		else:
			self.subjects = subjects

	def __str__(self):
		return f"Name : {self.name}\nId: {self.id}\nSubjects: {[sub for sub in self.subjects]}"



def create_students(num: int):
	li = []
	for stu in range(num):
		s = Student(f"Student {stu}", stu)
		li.append(s)
	return li

def divide_classes(classes_dict: dict, max_studens_per_class: int):
	diversed_classes = []
	for keys, values in classes_dict.items():
		if values/max_studens_per_class <= 1:
			diversed_classes.append(keys)
		else:
			classes_part = math.ceil(values / max_studens_per_class)
			for i in range(classes_part):
				diversed_classes.append(f"{keys} {i+1}")

	return diversed_classes


def all_students_per_subject(stu_arr: list[Student]):
	collection = dict()
	curr_sub_stu = 0
	for sub in subjects_list:
		for stu in stu_arr:
			if sub in stu.subjects:
				curr_sub_stu += 1
		# count for one sub is over
		collection[sub] = curr_sub_stu
		curr_sub_stu = 0 # resetting

	return collection


def run():
	# s1 = Student("Alan", 1)
	# print(s1)

	# random sample
	# sample = random.sample(subjects, 4)
	# print(sample)

	# create students
	li = create_students(100)
	# for i in li:
	# 	print(i)
	# 	print("**"*24)

	collection = all_students_per_subject(li)
	print(collection)
	classes = divide_classes(collection, 60)
	print(classes)




if __name__ == "__main__":
	run()

