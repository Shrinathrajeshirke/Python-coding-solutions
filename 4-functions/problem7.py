# > **Write Lambda functions for:**
# > - Square of a number
# > - Check even or odd
# > - Find maximum of two numbers
# > - Sort list of tuples by second element

sq_num = lambda x: x**2
print(sq_num(5))

even_odd = lambda x: "Even" if x%2==0 else "Odd"
print(even_odd(5))

max_num = lambda x, y: x if x>y else y
print(max_num(4,5))

students = [("Ram",85), ("Sam",92), ("Tom",67)]
students = sorted(students, key= lambda x: x[1])
print(f"sorted by Marks: {students}")