# File Deduplication Script Challenge

## Objective

Develop a script that identifies and removes duplicate files in a directory based on their content, not just their file names. You will need to use a hashing algorithm, such as SHA256, to compute the hash of the file content and determine if any duplicates exist.

## Requirements

- **Hashing Algorithm:** The script must compute a unique hash (e.g., SHA256) for each file to compare their contents.
- **Directory Input:** The script should accept a directory path as input where the files are stored.
- **Duplicate Identification:** Two or more files should be considered duplicates if they have the same hash value.
- **File Deletion:** The script must allow removing duplicates, with an option to either delete the duplicates automatically or list them for manual review.
- **Logging:** Log the results of the operation, including files found to be duplicates and any deletions that were made.
  - Have to use the logging library to log the results of the operation, including files found to be duplicates and any deletions that were made.

## Additional Features (Optional)
- Implement a command-line interface (CLI) to specify options such as:
  - Whether to delete duplicates automatically.
  - Whether to only list duplicates without removing them.
  - Whether to include hidden files in the scan.
- Allow the user to specify the hashing algorithm (e.g., SHA256, SHA1, MD5) via command-line arguments.

## Example Usage

### Command-Line Interface (CLI)
```bash
python deduplicate.py --directory /path/to/directory --delete
```

- `--directory`: The path to the directory where the files are located.
- `--delete`: Optional flag to delete duplicate files. If not provided, the script will only list duplicates without removing them.

### Example Output
```
Starting deduplication process in /path/to/directory...

Duplicate files found:
1. /path/to/directory/file1.txt
2. /path/to/directory/file2.txt

Deleting duplicate: /path/to/directory/file2.txt

Deduplication complete. 1 file(s) removed.
```

## Evaluation Criteria

- **Correctness:** Does the script correctly identify and remove duplicate files based on content?
- **Efficiency:** How well does the script handle large directories with many files?
- **Logging and Reporting:** Does the script provide clear logging of what it is doing and what changes were made?
- **Usability:** How easy is it to use the script? Is the command-line interface intuitive?
- **Code Quality:** Is the code clean, readable, and well-structured?