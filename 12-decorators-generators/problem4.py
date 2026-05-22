# Write a generator function called even_numbers that 
# yields even numbers up to a given limit.

def even_numbers(limit):
    for i in range(limit+1):
        if i%2==0:
            yield i

gen = even_numbers(10)
for num in gen:
    print(num)
