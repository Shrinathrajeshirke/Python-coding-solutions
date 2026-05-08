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

def phone_number_extractor(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

print("Output:")
phone_numbers_list = phone_number_extractor(text)
print(f"Found {len(phone_numbers_list)} phone numbers")
for phone in phone_numbers_list:
    print(phone)