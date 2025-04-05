import os

# Specify the directory path
directory_path = '/CLASS1'

# List all entries in the directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
