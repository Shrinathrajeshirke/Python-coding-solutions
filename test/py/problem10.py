# Write a function organize_files_by_type(folder_path) that:

# Scans all files in folder_path (non-recursive)
# Moves each file into a subfolder named after its extension (without the dot)
# Creates subfolders as needed
# Returns a dictionary where keys are extension names and values are lists of filenames moved there

from pathlib import Path
from collections import defaultdict

def organize_files_by_type(folder_path):
    result = defaultdict(list)
    p = Path(folder_path)
    files = p.rglob("*")
    files = [str(file) for file in files if file.is_file]
    for file in files:
        source_file = Path(file)
        extension = source_file.suffix
        extension = extension[1:]
        if extension not in [folder.name for folder in p.iterdir() if folder.is_dir()]:
            destination_folder =Path(extension)
            destination_folder.mkdir(parents=True, exist_ok=True)
            target_path = destination_folder / source_file.name
            source_file.rename(target_path)
            result[extension].append(source_file.name)
    return dict(result)
        
print(organize_files_by_type("D:/python_practice/test"))