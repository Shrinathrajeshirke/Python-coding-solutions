# > **Write a program that:**
# > - Takes N numbers from user
# > - Stores in a list
# > - Prints:
# >   - Even numbers from list
# >   - Odd numbers from list
# >   - Sum of even numbers
# >   - Sum of odd numbers

def num_sorting():
    n = int(input("Enter a number: "))

    num_list = []
    even_nums = []
    odd_nums = []

    for i in range(n):
        num_list.append(int(input("Enter a number: ")))

    for i in range(n):
        if num_list[i]%2==0:
            even_nums.append(num_list[i])
        else:
            odd_nums.append(num_list[i])

    print(f"Even numbers: {even_nums}")
    print(f"Odd numbers: {odd_nums}")
    print(f"Sum of even: {sum(even_nums)}")
    print(f"Sum of odd: {sum(odd_nums)}")

num_sorting()
        
