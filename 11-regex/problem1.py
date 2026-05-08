# Check if email is valid
# Pattern: username@domain.extension
# Username: letters, numbers, dots, underscores
# Domain: letters, numbers, dots, hyphens
# Extension: 2-6 letters


emails = [
    "john.doe@example.com",
    "alice_123@test.co.uk",
    "invalid@",
    "no-at-sign.com",
    "test@domain",
    "user@site.travel"
]

import re

def email_validator(email):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
    if re.match(pattern, email):
        print(f"{email} is Valid email.")
    else:
        print(f"{email} is Invalid email.")

print("Output:")
for email_id in emails:
    email_validator(email_id)
