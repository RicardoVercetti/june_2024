# rough_one.py
import itertools
import math

# Example list
# items = ["HISTORY", "MATH", "SCIENCE", "PE", "HEALTH", "GUIDANCE", "ELECTIVE", "CTE", "LUNCH"]
items = ['CHEMISTRY', "ENGLISH", "MATH", "LUNCH"]



# code segments

def all_possible_combinations(items: list[str]):
    permutations = list(itertools.permutations(items))
    li = []
    for p in permutations:
        li.append(p)
    return li

def all_possible_combinations_with_lunch(all_per_list: list[str], pos: int):
    new_list = []
    for l in all_per_list:
        if l[pos] == "LUNCH":
            new_list.append(l)
    return new_list

def for_fixed_number_of_classes(combos: list[str], no_of_classes:dict, per_day: int):
    # for number of classes, we have to break how many classes can be taken per day - say 4 per day(any combo)
    total_number_of_classes = 0
    for key, value in no_of_classes.items():
        total_number_of_classes += value
    print(f"Total number of classes : {total_number_of_classes}")
    deviced = math.ceil(total_number_of_classes/per_day)
    print(f"devisioned : {total_number_of_classes/per_day}")
    print(f"Ceil devisioned : {deviced}")


student_schedule_combinations = all_possible_combinations_with_lunch(all_possible_combinations(items=items), 2)

# 5 days a week, so 5 day combos of schedule
# conditions to be met:
#           1 - student schedule filling takes priority
#           2 - teachers assigned per day are not pushed after their minimum quotas


# for i in student_schedule_combinations:
#     print(i)

no_of_classes = {
    "CHEMISTRY": 46,
    "PHYSICS": 23,
    "GEOMENTRY": 44
}

for_fixed_number_of_classes(student_schedule_combinations, no_of_classes=no_of_classes, per_day=4)