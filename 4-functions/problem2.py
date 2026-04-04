# > **Write a function with default arguments:**
# > - Function called `greet_user`
# > - Parameters: name, language
# > - Default language = "English"
# > - Greet in different languages

def greet_user(name, language = "English"):
    if language == "English":
        print(f"Hello {name}! Good Morning!")
    elif language == "Hindi":
        print(f"Namaste {name}! Shubh Prabhat!")
    elif language == "Marathi":
        print(f"Namaskar {name}! Shubh Sakal!")
    else:
        print(f"{language} not found.")

greet_user("Ram", "Marathi")