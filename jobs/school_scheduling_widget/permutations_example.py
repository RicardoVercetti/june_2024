# permutations_example.py

import itertools
import math

# Define the names of men and women
men = ["M1", "M2", "M3", "M4", "M5"]
women = ["W1", "W2", "W3", "W4"]

# Calculate the number of arrangements
factorial_4 = math.factorial(4)
factorial_5 = math.factorial(5)
total_arrangements = factorial_4 * factorial_5

# print(f"The number of ways to arrange 5 men and 4 women so that women occupy the even places is: {total_arrangements}")


# Generate all possible permutations of men and women
men_permutations = list(itertools.permutations(men))
women_permutations = list(itertools.permutations(women))

# List to store the valid arrangements
valid_arrangements = []

# Create the valid arrangements
for men_perm in men_permutations:
    for women_perm in women_permutations:
        arrangement = [""] * 9  # Create an empty arrangement of 9 positions
        arrangement[0] = men_perm[0]
        arrangement[2] = women_perm[0]
        arrangement[4] = men_perm[1]
        arrangement[6] = women_perm[1]
        arrangement[8] = men_perm[2]
        arrangement[1] = men_perm[3]
        arrangement[3] = women_perm[2]
        arrangement[5] = men_perm[4]
        arrangement[7] = women_perm[3]
        valid_arrangements.append(arrangement)

# Print some of the valid arrangements
print("Some valid arrangements are:")
for i in range(min(5, len(valid_arrangements))):  # Print only the first 5 arrangements
    print(valid_arrangements[i])

