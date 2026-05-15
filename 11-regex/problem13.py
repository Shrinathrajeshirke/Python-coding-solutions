# Write a function that finds and masks credit card numbers in text.

# Given this text:

# Write a function mask_credit_cards(text) that:
# - Finds all valid credit card numbers (format: XXXX-XXXX-XXXX-XXXX)
# - Masks first 12 digits, keeps last 4 visible
# - Replaces each group with ****

import re

text = """
Customer 1: 1234-5678-9012-3456
Customer 2: 9876-5432-1098-7654
Customer 3: 1111-2222-3333-4444
Invalid: 1234-567-9012-3456
Invalid: 12345-678-9012-3456
"""

def credit_card_masking(text):
    pattern = r"(\d{4})-(\d{4})-(\d{4})-(\d{4})"
    replacement = r"****-****-****-\4"
    new_text = re.sub(pattern, replacement, text)
    return new_text.strip()

print(credit_card_masking(text))

