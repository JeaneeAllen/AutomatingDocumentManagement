# This script extracts the filename and extension from a given file path.

# Import necessary modules
import os # allows us to interact with the operating system
import sys # allows us to access system-specific parameters and functions

# Define a function to extract the filename and extension from a given file path
def extract_file_details(filename):

    base_name = os.path.basename(filename)
    name, extension = os.path.splitext(base_name)
    extension = extension.lstrip(".")

    return name, extension

# Check if the user provided a filename as an argument & test in Terminal with: python data_extract.py <filename or file path>
if len(sys.argv) != 2:
    print("Use: python data_extract.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

name, extension = extract_file_details(filename)
print(f"Input: {filename}")
print(f"Filename: {name}")

if extension:
    print(f"Extension: {extension}")
else:
    print("Extension: No extension found.")


# Two Methods to test Script:
    # 1. In Terminal: python data_extract.py <filename or file path>
    # 2. In Jupyter Notebook: Call the function with a filename or file path as an argument
        # Example: extract_file_details("example_file.txt") or extract_file_details("/path/to/example_file.txt")