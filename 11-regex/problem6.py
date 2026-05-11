# Remove/mask sensitive information
# Mask: credit cards, SSN, emails, phone numbers
# Replace with: [REDACTED]

text = """
Contact: john@example.com or 123-456-7890
Credit Card: 1234-5678-9012-3456
SSN: 123-45-6789
Email me at alice_test@site.org
"""

import re

def mask_info(text):
    masked_text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}", "[EMAIL]" , text)
    masked_text = re.sub(r"[0-9]{3}-[0-9]{2}-[0-9]{4}", "[SSN]", masked_text)
    masked_text = re.sub(r"[0-9]{3}-[0-9]{3}-[0-9]{4}","[PHONE]", masked_text)
    masked_text = re.sub(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", "[CREDIT_CARD]", masked_text)
    print("Output:")
    print(masked_text)

mask_info(text)