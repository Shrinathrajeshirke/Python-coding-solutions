# Find and Replace with Groups:

# Find dates in format DD-MM-YYYY
# Convert to MM/DD/YYYY (US format)
# Use capture groups and backreferences

text = """
Meeting on 25-12-2024
Deadline: 31-01-2025
Event: 15-08-2024
"""

import re

def date_replace(text):
    pattern = r"(\d{2})-(\d{2})-(\d{4})"
    replacement = r"\2/\1/\3"
    new_text = re.sub(pattern, replacement, text)
    return new_text.strip()

print(date_replace(text))