# Extract dates in different formats
# Convert all to standard format: YYYY-MM-DD
# Handle formats:

# DD-MM-YYYY
# DD/MM/YYYY
# MM-DD-YYYY
# YYYY-MM-DD

text = """
Meeting on 25-12-2024
Deadline: 01/06/2025
Started: 2024-03-15
Event on 12-31-2024
"""

import re

def date_formatting(text):
    pattern = r"(\d{2,4})[-/](\d{2})[-/](\d{2,4})"

    matches = re.findall(pattern, text)

    for match in matches:
        g1, g2, g3 = match

        if len(g1) == 4:
            year, month, day = g1, g2, g3
        
        elif len(g3) == 4:
            year = g3
            if int(g1)>12:
                day, month = g1, g2
            else:
                day, month = g2, g1

        original = f"{g1}-{g2}-{g3}"
        converted = f"{year}-{month}-{day}"
        print(f"{original} -> {converted}")

date_formatting(text)