import os

# Specify the directory (use '.' for the current directory)
directory_path = '.'

# List all files and folders in the directory
files = os.listdir(directory_path)

# Print the directory contents
print("Contents of Directory:", directory_path)
for file in files:
    print(file)
