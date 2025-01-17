# File Browser Solution

## Class

```python
class SkipThisFile(Exception):
    pass

class FileBrowser:
    def __init__(self, files):
        self.files = files

    def read_lines(self, file):
        with open(file, 'r') as f:
            for line in f:
                yield line.strip()

    def browse(self):
        for file in self.files:
            try:
                print(f"Browsing file: {file}")
                for line in self.read_lines(file):
                    user_input = input(line + "\nPress Enter for next line, 'n' + Enter to skip file: ")
                    if user_input == 'n':
                        raise SkipThisFile
            except SkipThisFile:
                print(f"Skipping file: {file}")
            except Exception as e:
                print(f"Error with file {file}: {e}")

if __name__ == "__main__":
    files = ['file1.txt', 'file2.txt']
    browser = FileBrowser(files)
    browser.browse()
```

---

## Function

```python
def read_lines(files):
    for file in files:
        try:
            print(f"Browsing file: {file}")
            with open(file, 'r') as f:
                for line in f:
                    yield file, line.strip()
        except Exception as e:
            print(f"Error with file {file}: {e}")
            continue

def browse_files(files):
    lines = list(read_lines(files))
    current_file = None
    index = 0

    while index < len(lines):
        file, line = lines[index]
        if file != current_file:
            current_file = file

        user_input = input(line + "\nPress Enter for next line, 'n' + Enter to skip file: ")
        if user_input == 'n':
            print(f"Skipping file: {file}")
            index = next((i for i, (f, _) in enumerate(lines) if f != file and i > index), len(lines))
        else:
            index += 1

if __name__ == "__main__":
    files = ['file1.txt', 'file2.txt']
    browse_files(files)
```

---

## Generator with Inline Interaction
```python
def read_lines_interactive(files):
    for file in files:
        try:
            print(f"Browsing file: {file}")
            with open(file, 'r') as f:
                for line in f:
                    user_input = input(line.strip() + "\nPress Enter for next line, 'n' + Enter to skip file: ")
                    if user_input == 'n':
                        print(f"Skipping file: {file}")
                        break
                    yield line.strip()
        except Exception as e:
            print(f"Error with file {file}: {e}")
            continue

if __name__ == "__main__":
    files = ['file1.txt', 'file2.txt']
    for line in read_lines_interactive(files):
        pass
```