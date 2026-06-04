# Write a function list_directory(path) that takes a folder path and returns a dictionary with two keys:

# "files" → a list of filenames that are files
# "folders" → a list of names that are directories

# If the path doesn't exist, return None.

from pathlib import Path

def list_directory(path):
    result = {}
    p = Path(path)
    if p.exists():
        dirs = p.iterdir()
        files = p.glob("*")
        subfolders = [dir.name for dir in dirs if dir.is_dir()]
        file_names = [file.name for file in files if file.is_file()]
        result["files"] = file_names
        result["folders"] = subfolders
        return result
    else:
        return None
    
print(list_directory("D:/python_practice/15-file-management"))