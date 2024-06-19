# rough_one.py
import itertools


# permutations

# from itertools import permutations
# p = [k for k in range(6)]
# for k in range(0,3):
#         p[k] = 1
# print(len(list(permutations(p))))
# for val in permutations(p):
# 	print(val)


# Example list
items = [1, 2, 3]


# Generate permutations
permutations = list(itertools.permutations(items))


# Print permutations
for p in permutations:
    print(p)



# print("Runs...")
