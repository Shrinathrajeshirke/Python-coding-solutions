# Problem 3
# Write a function create_folder_structure(base_path, structure) that takes:

# base_path — a string path where folders will be created
# structure — a list of folder names to create inside base_path

# The function should:

# Create base_path if it doesn't exist
# Create each folder in the list inside base_path
# Return a list of full paths (as strings) of successfully created folders

from pathlib import Path

def create_folder_structure(base_path, structure):
    p = Path(base_path)
    folders = []
    p.mkdir(parents=True, exist_ok=True)
    for subfolder in structure:
        foldername = p/subfolder
        foldername.mkdir(parents=True, exist_ok=True)
        folders.append(str(foldername))
    return folders

print(create_folder_structure("D:/python_practice/test", ["docs", "images", "logs"]))