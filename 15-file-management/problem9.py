# Write a function clean_empty_folders(folder_path) that:

# Recursively finds all empty folders inside folder_path
# Deletes them
# Returns a list of folder paths (as strings) that were deleted

from pathlib import Path

def clean_empty_folders(folder_path):
    empty_folders = []
    p = Path(folder_path)
    
    for folder in sorted(p.rglob("*"), reverse=True):
        if folder.is_dir() and not list(folder.iterdir()):
            empty_folders.append(str(folder))
            folder.rmdir()
    return empty_folders

print(clean_empty_folders("D:/python_practice/14-mini-project"))