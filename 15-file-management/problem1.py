# Write a function called get_file_info(filepath) that takes a file path string and returns a dictionary with these keys:

# "name" → the filename with extension
# "stem" → the filename without extension
# "extension" → the file extension (e.g. .txt)
# "size" → file size in bytes (0 if file doesn't exist)
# "exists" → boolean, whether the file exists

from pathlib import Path

def get_file_info(filepath):
    p = Path(filepath)
    filename = p.name
    file = p.stem
    ext = p.suffix
    if p.exists():
        filesize = p.stat().st_size
    else:
        filesize = 0
    return f"Filename: {filename}, Filename without extension: {file}, Extension: {ext}, File size: {filesize} bytes, file exists: {p.exists()}"

print(get_file_info("D:/python_practice/15-file-management/intro.txt"))