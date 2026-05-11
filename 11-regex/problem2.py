# Extract all phone numbers from text
# Formats to match:

# 123-456-7890
# (123) 456-7890
# 123.456.7890
# 1234567890

text = """
Contact us at 123-456-7890 or (987) 654-3210.
You can also call 555.123.4567 or 9876543210.
Invalid: 12-345-6789 (too short)
"""

import re

def extract_phone_numbers(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    matches = re.findall(pattern, text)
    return matches

print("Output:")
phone_numbers_list = extract_phone_numbers(text)
print(f"Found {len(phone_numbers_list)} phone numbers")
for i, phone in enumerate(phone_numbers_list,1):
    print(f"{i}. {phone}")