# Write a function watch_directory_changes(folder_path, seconds) that:

# Takes a folder path and a number of seconds
# Captures a snapshot of all files in the folder at start
# Waits for seconds using time.sleep()
# Captures another snapshot after waiting
# Returns a dictionary with:

# "added" → list of files added
# "removed" → list of files removed

from pathlib import Path
import time

def watch_directory_changes(folder_path, seconds):
    p = Path(folder_path)
    files = p.glob("*")
    old_files = [file.name for file in files if file.is_file()]
    time.sleep((seconds))
    files = p.glob("*")
    new_files = [file.name for file in files if file.is_file()]
    return {"added": [name for name in new_files if name not in old_files],
            "removed": [name for name in old_files if name not in new_files]}

print(watch_directory_changes("D:/python_practice/14-mini-project", 10))
