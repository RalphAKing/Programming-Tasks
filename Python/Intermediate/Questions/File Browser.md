# File Browser

## Objective
Develop a program that enables interactive browsing of file content, displaying one line at a time with user-defined controls.

## Features

### Interactive Controls
1. **Next Line**: Press `Enter` to display the next line.
2. **Skip File**: Press `n` + `Enter` to move to the next file.
3. **Other Inputs**: Any other key + `Enter` acts as `Enter`.

### Generator-Based Design
- Implements a `read_lines` generator to handle files efficiently, line by line.
- Includes a custom `SkipThisFile` exception to allow skipping the current file programmatically.

## Example Files

### `file1.txt`
```
Line 1 of File 1
Line 2 of File 1
Line 3 of File 1
```

### `file2.txt`
```
Line 1 of File 2
Line 2 of File 2
```

---

## Example Console Session

### Interaction Log
```text
Line 1 of File 1
Press Enter for next line, 'n' + Enter to skip file: 
```

*User presses `Enter`*
```text
Line 2 of File 1
Press Enter for next line, 'n' + Enter to skip file: 
```

*User presses `n`*
```text
Line 1 of File 2
Press Enter for next line, 'n' + Enter to skip file: 
```

*User presses `Enter`*
```text
Line 2 of File 2
Press Enter for next line, 'n' + Enter to skip file: 
```

*User presses `Enter` again*
```text
[End of files]
```

---

## Functional Requirements

### File Handling
1. Process files in the order they are provided as command-line arguments.
2. Handle errors such as missing files or read errors gracefully.

### User Interaction
- `Enter`: Moves to the next line.
- `n + Enter`: Skips to the next file.
- Other inputs are treated like `Enter`.

### Exception Handling
- Custom `SkipThisFile` exception for skipping the current file.

---

## Program Design

### `read_lines` Generator
- Reads each file line by line.
- Yields lines to the main program.
- Raises `SkipThisFile` if requested.

### User Interaction Loop
- Uses the generator to display lines.
- Responds to user input to determine the next action.
