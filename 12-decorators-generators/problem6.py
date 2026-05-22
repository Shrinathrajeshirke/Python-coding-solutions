# Write a generator function called counter that yields 
# numbers infinitely from a start value with a given step.

def counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step

gen = counter(start=5, step=3)
print(next(gen))  # 5
print(next(gen))  # 8
print(next(gen))  # 11
print(next(gen))  # 14

gen2 = counter()
print(next(gen2))  # 0
print(next(gen2))  # 1
print(next(gen2))  # 2