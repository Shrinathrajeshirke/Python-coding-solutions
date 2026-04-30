# Create a menu generator
# Categories: Appetizer, Main, Dessert
# Generate all possible meal combinations

appetizers = ["Salad", "Soup"]
mains = ["Pasta", "Steak", "Fish"]
desserts = ["Cake", "Ice Cream"]

import itertools

def menu_generator(appetizers, mains, desserts):
    products = list(itertools.product(appetizers, mains, desserts))
    combs = 0
    print("Output")
    print("All meal combinations: ")
    for i, product in enumerate(products):
        combs += 1
        print(f"\nCombo {i+1}")
        appetizer, main, dessert = product
        print(f"Appetizer: {appetizer}")
        print(f"Main: {main}")
        print(f"dessert: {dessert}")
    print(f"\nTotal combinations: {combs}")

menu_generator(appetizers, mains, desserts)