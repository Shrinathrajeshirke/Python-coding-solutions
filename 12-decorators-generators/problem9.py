# Write a generator function called read_in_chunks that 
# reads a large text and yields it one line at a time,
# skipping empty lines and stripping whitespace.

text = """
Python is amazing.

Generators are memory efficient.

Decorators add functionality.

This is the last line.
"""

def read_in_chunks(text):
    text = "\n".join([line for line in text.split("\n") if line.strip()])
    for line in text.splitlines():
        yield line

for line in read_in_chunks(text):
    print(line)