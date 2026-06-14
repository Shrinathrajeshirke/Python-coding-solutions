# Write a function organize_files_by_type(folder_path) that:

# Scans all files in folder_path (non-recursive)
# Moves each file into a subfolder named after its extension (without the dot)
# Creates subfolders as needed
# Returns a dictionary where keys are extension names and values are lists of filenames moved there

from pathlib import Path
from collections import defaultdict
import shutil

def organize_files_by_type(folder_path):
    result = defaultdict(list)
    p = Path(folder_path)
    files = p.glob("*")
    for file in files:
        if file.is_file():
            extension = file.suffix[1:]
            if not extension:
                extension = "no_extension"
            destination_folder = p /extension
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(destination_folder / file.name))
            result[extension].append(file.name)
    return dict(result)
        
print(organize_files_by_type("D:/python_practice/test"))