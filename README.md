# File Organizer Script

This Python script automatically organizes files in a specified directory by moving them into subdirectories based on their file extensions. It can handle common file types like PDF, TXT, DOCX, PPTX, and others. If the necessary subdirectories don't exist, the script will create them.

## Features
- **Automatic File Organization**: Moves files into directories based on their file extension.
- **Directory Creation**: Automatically creates target directories if they don't exist.
- **Error Handling**: Handles common errors like permission issues or missing directories.
- **Customizable**: You can easily add new file extensions and target directories as needed.

## How It Works
The script checks the file extension of each file in the specified directory and moves it to a corresponding subdirectory:
- `.pdf` files go to the **Pdfs** folder
- `.txt` files go to the **Text_files** folder
- `.docx` files go to the **Documents** folder
- `.pptx` files go to the **Presentations** folder
- Any other file types go to the **Others** folder

## Setup and Usage

### Requirements
- Python 3.x

### Usage
1. Open the script file and set the `main_dir` variable to the path of the directory you want to organize.
   ```python
   main_dir = 'path/to/directory'
