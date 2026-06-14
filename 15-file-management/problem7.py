# Write a function get_directory_stats(folder_path) that returns a dictionary with:

# "total_files" → total number of files (recursively)
# "total_folders" → total number of subfolders (recursively)
# "total_size_kb" → total size of all files in KB (rounded to 2 decimals)
# "largest_file" → filename of the largest file

from pathlib import Path

def get_directory_stats(folder_path):
    p = Path(folder_path)
    files = p.rglob("*")
    subfolders = p.iterdir()

    file_names = [str(file) for file in files if file.is_file()]
    subfolders = [str(subfolder) for subfolder in subfolders if subfolder.is_dir()]
    total_size = 0
    large_file_size = 0
    largest_file = ""
    for file in file_names:
        f = Path(file)
        size = f.stat().st_size 
        if size > large_file_size:
            large_file_size = size
            largest_file = f.name
        total_size += f.stat().st_size
    return {"total_files":len(file_names), "total_folders":len(subfolders), "total_size_kb": round(total_size/1024,2), "largest_file": largest_file}

print(get_directory_stats("D:/python_practice/14-mini-project"))
