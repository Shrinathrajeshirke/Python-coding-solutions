# Write a recursive function that:

# Takes a list of numbers
# Returns sum of EVEN numbers only
# Using recursion!

def sum_of_even(ls):
    sum = 0
    if ls == []:
        return 0
    if ls[0]%2==0:
        sum += ls[0]
        
        
    
print(sum_of_even[3])