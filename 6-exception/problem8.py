# Write a program that:

# Creates a custom exception AgeError
# Function check_age(age) that:

# Raises AgeError if age < 0
# Raises AgeError if age > 120
# Returns "Minor" if age < 18
# Returns "Adult" if age >= 18


# Handle the custom exception

class AgeError(Exception):
    pass 

def check_age(age):
    if age < 0:
        raise AgeError("Age can't be negative")

    if age > 120:
        raise AgeError("Age can't be more than 120")
    
    if age < 18:
        return "Minor"
    else:
        return "Adult"

ages = [-12, 12, 24, 121]

for age in ages:
    try:
        print(check_age(age))
    except AgeError as e:
        print(f"Custom Error: {e}")
