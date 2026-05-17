# %% [markdown]
# # Week 1 Assignment: Automating Document Management in Data-Intensive Business Setup
# ***
# 
# **Task:** 
# *Develop a Python script that assists in managing a document repository. The script should be capable of processing a list of file names and extracting the filename (without the extension) and the file extension.*
# 
# **Task Details:** 
# - Input: Your script should take a string input representing a file path or a filename, such as "meeting_notes_2023.pdf".
# - Output: Your script should output the filename without the extension ("meeting_notes_2023") and the file extension ("pdf").
# ***

# %% [markdown]
# ➡️ **Step 1:** Import Necessary Modules: Import the required Python modules at the beginning of your script, such as `os` if needed for path operations.

# %%
import os # allows us to interact with the operating system

# %% [markdown]
# ***
# ➡️  **Step 2:** Create a Function to Extract Information: Write a function named `extract_file_details(filename)` that takes a single string argument representing the file path or name and returns two items: the name and the extension (both strings)   
# ➡️  **Step 3:** Implement Filename and Extension Extraction: Inside the function, use string methods or regular expressions to separate the filename from its extension and return both values.   

# %%
def extract_file_details(filename):
    """
    Extract the filename without its extension and the file extension.

    Args:
        filename (str): A file path or filename, such as "meeting_notes_2023.pdf".

    Returns:
        tuple: Two strings:
            - filename without the extension
            - file extension without the dot
    """
    base_name = os.path.basename(filename)
    name, extension = os.path.splitext(base_name)

    # Remove the leading dot from the extension
    extension = extension.lstrip(".")

    return name, extension

# %% [markdown]
# ***
# ➡️  **Step 4:** Handle Edge Cases: Ensure your function correctly handles filenames with multiple periods or no extension.
# - We only want the function to execute if the path provided exists AND is a directory. If the path does not exist or leads to a file → provide an error statement.  
#   
# ➡️  **Testing Your Script:**
# - Sample Input: Use provided examples like "meeting_notes_2023.pdf" and other varied filenames to test your script.
# - Validate Outputs: Check that your function returns the correct filename and file extension separately.
# - Edge Cases: Test filenames with no extensions, multiple extensions, and unusual characters to ensure robustness.

# %%
test_files = [
    "meeting_notes_2023.pdf",
    "report.final.version.docx",
    "budget_summary.xlsx",
    "/Users/jen/Documents/project_notes.txt",
    "archive.tar.gz",
    "my file name.pdf",
    "data_backup_2026.csv"
]

for file in test_files:
    name, extension = extract_file_details(file)
    print(f"Input: {file}")
    print(f"Filename: {name}")
    print(f"Extension: {extension}")
    print()

# %% [markdown]
# ***
# J. Allen   
# CSP Wk 1 Assignment   
# 05/17/2026   
# **github:** https://github.com/JeaneeAllen/AutomatingDocumentManagement


