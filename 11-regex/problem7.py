# Parse server log entries
# Extract: timestamp, log level, message
# Count logs by level
# Find errors

import re
from collections import Counter

logs = """
2024-01-15 10:30:45 [INFO] Server started successfully
2024-01-15 10:31:12 [ERROR] Database connection failed
2024-01-15 10:31:45 [WARNING] High memory usage detected
2024-01-15 10:32:01 [INFO] Request processed
2024-01-15 10:32:15 [ERROR] File not found: config.json
2024-01-15 10:33:00 [DEBUG] Processing user request
"""

def server_log_extraction(text):
    pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)"

    matches = re.finditer(pattern, text)

    log_entries = []
    levels = []
    errors = []
    
    for match in matches:
        date = match.group('date')
        time = match.group('time')
        level = match.group('level')
        message = match.group('message')
        
        log_entries.append((date, time, level, message))

        if level == "ERROR":
            errors.append((time, message))
    
    level_count = Counter(levels)

    print("Parsed logs:")
    for date, time, level, message in log_entries:
        print(f"{date} {time} | {level} | {message}")

    print("\nLog Level Count:")
    for level, count in level_count.items():
        print(f"{level}: {count}")

    print("\nErrors found:")
    for time, message in errors:
        print(f"[{time}] {message}")

server_log_extraction(logs)