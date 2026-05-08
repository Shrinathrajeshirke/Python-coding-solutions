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
        checks+= 1

    if re.search(r"[A-Z]", password):
        checks += 1
    
    if re.search(r"[a-z]", password):
        checks += 1

    if re.search(r"\d", password):
        checks += 1
    
    if re.search(r"[!@#$%*?&_]", password):
        checks += 1

    if checks == 5:
        return "Strong"
    elif checks >= 3:
        return "Medium"
    else:
        return "Weak"
    
for password in passwords:
    print(password_strength_checker(password))