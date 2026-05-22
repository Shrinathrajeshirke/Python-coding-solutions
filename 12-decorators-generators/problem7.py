# Create a pipeline of generators that process data 
# step by step.

# Write three generators:
# 1. numbers(n) - yields numbers from 1 to n
# 2. square(gen) - takes a generator, yields squared values
# 3. even_filter(gen) - takes a generator, yields only even values

def numbers(n):
    for i in range(1,n+1):
        yield i

def squares(gen):
    for i in gen:
        yield i**2

def even_filter(gen):
    for i in gen:
        if i%2==0:
            yield i

pipeline = even_filter(squares(numbers(10)))

for num in pipeline:
    print(num)