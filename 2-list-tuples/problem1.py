# Write a program that:

# Creates a list of 5 fruits
# Prints first and last fruit
# Prints first 3 fruits
# Prints last 3 fruits
# Prints list in reverse

fruits = ["apple","banana","mango","orange","grape"]

print(f"first fruit: {fruits[0]}")

print(f"last fruit: {fruits[-1]}")

print(f"first 3 fruits: {fruits[:3]}")

print(f"last 3 fruits: {fruits[-3:]}") ## use negative indexing for last

print(f"reversed fruit list: {fruits[::-1]}")