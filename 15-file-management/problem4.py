# Write a function find_files_by_extension(folder_path, extension) that:

# Takes a folder path and a file extension (e.g. ".txt")
# Searches recursively through all subfolders
# Returns a list of full file paths (as strings) matching that extension
# Returns an empty list if none found or path doesn't exist

from pathlib import Path

def find_files_by_extension(folder_path, extension):
    p = Path(folder_path)
    if not p.exists():
        result = []
    else:
        files = Path(folder_path).rglob(f"*{extension}")
        result = []
        for file in files:
            result.append(str(file))
    return result

print(find_files_by_extension("D:/python_practice", ".txt"))
