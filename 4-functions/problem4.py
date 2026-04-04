# > **Write a function using \*\*kwargs:**
# > - Function called `create_profile`
# > - Takes any keyword arguments
# > - Prints a formatted user profile


def create_profile(**kwargs):
    if not kwargs:
        print("No details provided")
        return 
    print("======== USer Profile =======")
    for key, value in kwargs.items():
        print(f"{key.capitalize():12}: {value}")
    
    print("==============================")

create_profile(
    name="Shrinath",
    age=20,
    city="Nashik",
    profession="Student",
    hobby="Coding"
)

