# Problem 5
# Write a function backup_files(source_folder, dest_folder) that:

# Copies all files (not folders) from source_folder to dest_folder
# Creates dest_folder if it doesn't exist
# Returns a dictionary with:

# "copied" → list of filenames successfully copied
# "failed" → list of filenames that failed

from pathlib import Path
import shutil
from collections import defaultdict

def backup_files(source_folder, dest_folder):
    dest = Path(dest_folder)
    source = Path(source_folder)
    dest.mkdir(parents=True, exist_ok=True)
    result = defaultdict(list)

    for item in source.iterdir():
        if item.is_file():
            file_name = item.name
            try:
                shutil.copy(item, dest)
                if (dest / file_name).exists():
                    result["copied"].append(file_name)
                else:
                    result["failed"].append(file_name)
            except Exception:
                result["failed"].append(file_name)
    return dict(result)

print(backup_files("D:/python_practice/source_dir", "D:/python_practice/dest_dir"))

    
