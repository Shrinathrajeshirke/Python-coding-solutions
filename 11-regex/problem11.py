# Write a function log_parser(text) that returns a dictionary with:
# - "errors": list of error messages (just the message part)
# - "warnings": list of warning messages (just the message part)
# - "dates": list of unique dates found (no duplicates)

import re
from collections import defaultdict

text = """
ERROR 2024-01-15 10:23:45 - Database connection failed
INFO 2024-01-15 10:24:01 - Server started successfully
WARNING 2024-01-16 09:15:30 - Memory usage high
ERROR 2024-01-16 11:45:22 - Timeout occurred
INFO 2024-01-17 08:00:00 - Backup completed
"""

def log_parser(text):
    pattern = r"(?P<level>[A-Z]+) (?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) - (?P<message>.*)"

    matches = re.finditer(pattern, text)

    log_entries = []
    messages = defaultdict(list)
    
    for match in matches:
        level = match.group('level')
        date = match.group('date')
        time = match.group('time')
        message = match.group('message')

        log_entries.append((level, date, time, message))

    for entry in log_entries:
        if entry[0] == 'ERROR':
            messages['errors'].append(entry[3])
        if entry[0] == 'WARNING':
            messages['warnings'].append(entry[3])
        if entry[1] not in messages['dates']:
            messages['dates'].append(entry[1])
        
    return dict(messages)

print(log_parser(text))


