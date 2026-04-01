# > **Write a program that:**
# > - Takes a list of numbers
# > - Groups them into 3 separate lists:
# >   - Divisible by 3
# >   - Divisible by 5
# >   - Divisible by both 3 and 5


def grouping_list():
    numbers = [1,3,5,9,10,15,20,21,25,30,45]

    divisible_by_3 = []
    divisible_by_5 = []

    divisible_by_3_and_5 = []

    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            divisible_by_3_and_5.append(number)
        elif number % 3 == 0:
            divisible_by_3.append(number)
        elif number % 5 == 0:
            divisible_by_5.append(number)
        
    print(f"Divisible by 3 only: {divisible_by_3}")
    print(f"Divisible by 5 only: {divisible_by_5}")
    print(f"Divisible by 3 and 5: {divisible_by_3_and_5}")
        
grouping_list()

    