# AST Part 1
 CST-301 AST project
Certainly! Here's a README file for your code:

---

# Java AST Exporter

## Overview
This Python script is designed to parse Java code and export its Abstract Syntax Tree (AST) to a JSON file. It utilizes the `javalang` library to parse the Java code and convert the resulting AST into a serializable format.

## Contributors
- Jordan Scott
- David Smical
- Eli Streitmatter

## Requirements
- Python 3.x
- javalang library (`pip install javalang`)

## Usage
1. Ensure you have Python 3.x installed on your system.
2. Install the `javalang` library by running `pip install javalang` in your terminal.
3. Update the `java_file_path` variable in the script to point to the Java file you want to parse.
4. Run the script using `python <script_name>.py`.
5. The script will generate a JSON file containing the AST of the Java code at the specified location.

## Example
```python
python ASTree301.py
```

## Output
The script will generate a JSON file containing the AST of the Java code. By default, the JSON file will be named `output_ast.json` and saved to the desktop. You can modify the `json_file_path` variable in the script to change the output location.

## Notes
- This script assumes that the input Java file is correctly formatted and syntactically valid.
- Ensure that the `javalang` library is installed and accessible in your Python environment.
