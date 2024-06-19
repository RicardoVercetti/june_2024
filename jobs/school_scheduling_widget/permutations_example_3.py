# permutations_example_3.py

import itertools

# Define the children
children = ['A', 'B', 'C', 'D', 'E', 'F']

# Part (i): Two particular children (A and B) are always together
# Treat 'A' and 'B' as a single unit
units = [('A', 'B'), ('B', 'A')]
remaining_children = ['C', 'D', 'E', 'F']

# Generate permutations of the 5 units
permutations_with_together = []
for perm in itertools.permutations(remaining_children + ['AB']):
    for unit in units:
        result = []
        for item in perm:
            if item == 'AB':
                result.extend(unit)
            else:
                result.append(item)
        permutations_with_together.append(result)

# Print the results
print("Permutations where A and B are always together:")
for perm in permutations_with_together:
    print(perm)
print(f"Total permutations where A and B are together: {len(permutations_with_together)}")

# Part (ii): Two particular children (A and B) are never together
# Generate all permutations of 6 children
# all_permutations = list(itertools.permutations(children))

# # Filter out permutations where A and B are together
# permutations_without_together = [
#     perm for perm in all_permutations
#     if not any(perm[i] == 'A' and perm[i + 1] == 'B' or perm[i] == 'B' and perm[i + 1] == 'A' for i in range(len(perm) - 1))
# ]

# # Print the results
# print("Permutations where A and B are never together:")
# for perm in permutations_without_together:
#     print(perm)
# print(f"Total permutations where A and B are never together: {len(permutations_without_together)}")
