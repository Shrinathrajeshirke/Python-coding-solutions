# Write a recursive function that:

# Takes a list of numbers
# Returns sum of EVEN numbers only
# Using recursion!

def sum_of_even(ls):
    if ls == []:
        return 0
    if ls[0] % 2 == 0:
        return ls[0] + sum_of_even(ls[1:])
    else:
        return sum_of_even(ls[1:])
         
    
print(sum_of_even([1,2,3,4]))