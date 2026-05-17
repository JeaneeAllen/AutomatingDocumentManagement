## Automating Document Management

# Objective:
This assignment aims for learners to reinforce Python refresher with additional practice. This assignment is intended as a Python refresher and does NOT require advanced NLP libraries such as NLTK or spaCy. Standard Python functionality (os, pathlib, string methods, regex, etc.) is sufficient. 

# Task
Develop a Python script that assists in managing a document repository. The script should be capable of processing a list of file names and extracting the filename (without the extension) and the file extension.

# Task Details:

- Input: Your script should take a string input representing a file path or a filename, such as "meeting_notes_2023.pdf".
- Output: Your script should output the filename without the extension ("meeting_notes_2023") and the file extension ("pdf").

# Guidelines

Script Development:

- Step 1: Import Necessary Modules: Import the required Python modules at the beginning of your script, such as `os` if needed for path operations.
- Step 2: Create a Function to Extract Information: Write a function named `extract_file_details(filename)` that takes a single string argument representing the file path or name and returns two items: the name and the extension (both strings)
- Step 3: Implement Filename and Extension Extraction: Inside the function, use string methods or regular expressions to separate the filename from its extension and return both values.
- Step 4: Handle Edge Cases: Ensure your function correctly handles filenames with multiple periods or no extension.