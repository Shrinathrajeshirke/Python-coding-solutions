# Write a function merge_text_files(file_list, output_file) that:

# Takes a list of text file paths and merges their content into one output file
# Each file's content should be separated by a newline and the filename as a header like --- filename.txt ---
# Returns the total number of lines written to the output file
# Skips files that don't exist

from pathlib import Path

def merge_text_files(file_list, output_file):
    p_out = Path(output_file)
    total_lines = 0
    with open(p_out, "w", encoding="utf-8") as f:
        for file in file_list:
            p = Path(file)
            if not p.exists():
                continue
            content = p.read_text(encoding="utf-8")
            header = f"--- {p.name} ---"
            f.write(header)
            f.write(content + "\n")
            total_lines += 1 + len(content.strip().split("\n"))
    return total_lines

file_list = [
    "D:/python_practice/intro.txt",
    "D:/python_practice/notes.txt"
]
output_file = "D:/python_practice/merged.txt"

print(merge_text_files(file_list, output_file))
