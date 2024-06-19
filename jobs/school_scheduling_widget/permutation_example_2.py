# permutation_example_2.py
import itertools

# Define the string array
chars = ['a', 'b', 'c', 'd', 'e']

# Generate all permutations of 3 characters from the string array
permutations = list(itertools.permutations(chars, 3))

# Print the permutations
for perm in permutations:
    print(''.join(perm))

# Optionally, print the number of permutations
print(f"Total number of permutations: {len(permutations)}")
