# Take a list of numbers
# Find all pairs (2 numbers) that sum to target
# Use combinations to check all pairs

numbers = [1, 2, 3, 4, 5, 6]
target = 7

import itertools

def sum_to_target(numbers, target):
    combs = itertools.combinations(numbers, 2)
    count = 0
    print("Output")
    print("Pairs that sum to 7:")
    for comb in combs:
        if sum(comb) == target:
            print(f"{comb} -> {comb[0]} + {comb[1]} = {target}")
            count += 1
    print(f"\nTotal pairs found: {count}")

sum_to_target(numbers, target)