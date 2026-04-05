# > **Write a function that takes another function as argument:**
# > - Function called `apply_operation`
# > - Takes a list and a function
# > - Applies that function to every element
# > - Returns new list


square = lambda x: x**2
double = lambda x: x*2
even = lambda x: True if x%2==0 else False

def apply_operation(ls, fn):
    result = []
    for num in ls:
        result.append(fn(num))
    return result

numbers = [1, 2, 3, 4, 5]
print(f"Square of numbers: {apply_operation(numbers, square)}")
print(f"double of numbers: {apply_operation(numbers, double)}")
print(f"Even numbers: {apply_operation(numbers, even)}")

