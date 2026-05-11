# Check password strength using regex
# Rules:

# At least 8 characters
# At least 1 uppercase letter
# At least 1 lowercase letter
# At least 1 digit
# At least 1 special character (@$!%*?&)


# Return strength: Weak, Medium, Strong

passwords = [
    "Pass123!",
    "weakpass",
    "NOLOWER123!",
    "NoDigits!",
    "Strong@Pass123",
    "Short1!"
]

import re

def password_strength_checker(password):

    checks = 0

    if len(password)>=8:
        checks += 1
    
    if re.search(r"[a-z]", password):
        checks += 1

    if re.search(r"[A-Z]", password):
        checks += 1

    if re.search(r"[0-9]", password):
        checks += 1

    if re.search(r"[@$!%*?&]", password):
        checks += 1
    
    if checks == 5:
        print(f"'{password}' strength is strong")
    elif checks >= 3:
        print(f"'{password}' strength is medium")
    else:
        print(f"'{password}' strength is weak")
    
for password in passwords:
    password_strength_checker(password)

