# Write a function that validates usernames based on rules.

# Given a list of usernames, validate each one against these rules:
# - Must be 3-16 characters long
# - Can only contain letters, numbers, and underscores
# - Must start with a letter
# - Cannot end with an underscore

import re
from collections import defaultdict

usernames = [
    "john_doe",
    "1john",
    "ab",
    "valid_user123",
    "invalid__user",
    "toolongusernamethatexceedslimit",
    "john_",
    "VALID_USER",
    "_invalid",
    "perfect1"
]

def username_validator(name_list):
    pattern = r"^([a-zA-Z])[a-zA-Z0-9_]{1,14}[a-zA-Z0-9]$"
    result = defaultdict(list)

    for name in name_list:
        if re.match(pattern, name):
            result['valid'].append(name)
        if not re.match(pattern, name):  
            result['invalid'].append(name)
    
    return dict(result)

print(username_validator(usernames))