# > **Write a program that:**
# > - Creates a list of 10 numbers
# > - Without using sort()
# > - Find and print:
# >   - Minimum value and its index
# >   - Maximum value and its index
# >   - Second minimum value
# >   - Second maximum value

def index_value():
    numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10]

    numbers_copy = numbers.copy()

    for j in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers_copy[i] > numbers_copy[i+1]:
                numbers_copy[i], numbers_copy[i+1] = numbers_copy[i+1], numbers_copy[i]

    min_val = numbers_copy[0]
    max_val = numbers_copy[-1]

    second_min = numbers_copy[1]
    second_max = numbers_copy[-2]

    print(f"Minimum: {min_val} at index {numbers.index(min_val)}")
    print(f"Maximum: {max_val} at index {numbers.index(max_val)}")

    print(f"Second minimum: {second_min}")
    print(f"second maximum: {second_max}")

index_value()


##another approach

# def index_value():
#     numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10]

#     # Find min and max manually
#     min_val = numbers[0]
#     max_val = numbers[0]
#     min_idx = 0
#     max_idx = 0

#     for i in range(len(numbers)):
#         if numbers[i] < min_val:
#             min_val = numbers[i]
#             min_idx = i
#         if numbers[i] > max_val:
#             max_val = numbers[i]
#             max_idx = i

#     # Find second min and max
#     second_min = None
#     second_max = None
#     for num in numbers:
#         if num != min_val:
#             if second_min is None or num < second_min:
#                 second_min = num
#         if num != max_val:
#             if second_max is None or num > second_max:
#                 second_max = num

#     print(f"Minimum: {min_val} at index {min_idx}")
#     print(f"Maximum: {max_val} at index {max_idx}")
#     print(f"Second Minimum: {second_min}")
#     print(f"Second Maximum: {second_max}")

# index_value()