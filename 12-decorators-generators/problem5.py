# Write a generator function called fibonacci that 
# yields fibonacci numbers up to n terms.

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a+b

for num in fibonacci(8):
    print(num)