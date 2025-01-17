# Logging Decorator Challenge Solution

## Basic Solutions

### Class

```python
import os
import hashlib
import logging

class FileDeduplicator:
    def __init__(self, directory):
        self.directory = directory
        self.duplicate_files = []

    def calculate_hash(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()

    def find_duplicates(self):
        hash_map = {}
        for root, _, files in os.walk(self.directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_hash = self.calculate_hash(file_path)
                if file_hash in hash_map:
                    self.duplicate_files.append(file_path)
                else:
                    hash_map[file_hash] = file_path

    def remove_duplicates(self, delete=False):
        self.find_duplicates()
        if delete:
            for duplicate_file in self.duplicate_files:
                os.remove(duplicate_file)
                logging.info(f"Deleted duplicate: {duplicate_file}")
            logging.info(f"Deduplication complete. {len(self.duplicate_files)} file(s) removed.")
        else:
            logging.info("Duplicates found:")
            for duplicate_file in self.duplicate_files:
                logging.info(f"- {duplicate_file}")

if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(description="File Deduplication Script")
    parser.add_argument("--directory", type=str, help="Directory path for deduplication")
    parser.add_argument("--delete", action="store_true", help="Delete duplicate files if set")
    args = parser.parse_args()

    deduplicator = FileDeduplicator(args.directory)
    deduplicator.remove_duplicates(delete=args.delete)
```

### Function

```python
import os
import hashlib
import logging

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_duplicates(directory):
    hash_map = {}
    duplicate_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)
            if file_hash in hash_map:
                duplicate_files.append(file_path)
            else:
                hash_map[file_hash] = file_path
    
    return duplicate_files

def remove_duplicates(duplicate_files, delete=False):
    if delete:
        for duplicate_file in duplicate_files:
            os.remove(duplicate_file)
            logging.info(f"Deleted duplicate: {duplicate_file}")
        logging.info(f"Deduplication complete. {len(duplicate_files)} file(s) removed.")
    else:
        logging.info("Duplicates found:")
        for duplicate_file in duplicate_files:
            logging.info(f"- {duplicate_file}")

if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(description="File Deduplication Script")
    parser.add_argument("--directory", type=str, help="Directory path for deduplication")
    parser.add_argument("--delete", action="store_true", help="Delete duplicate files if set")
    args = parser.parse_args()

    duplicate_files = find_duplicates(args.directory)
    remove_duplicates(duplicate_files, delete=args.delete)
```

### Procedural

```python
import os
import hashlib
import logging

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_duplicates(directory):
    hash_map = {}
    duplicate_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)
            if file_hash in hash_map:
                duplicate_files.append(file_path)
            else:
                hash_map[file_hash] = file_path
    
    return duplicate_files

def remove_duplicates(duplicate_files, delete=False):
    if delete:
        for duplicate_file in duplicate_files:
            os.remove(duplicate_file)
            logging.info(f"Deleted duplicate: {duplicate_file}")
        logging.info(f"Deduplication complete. {len(duplicate_files)} file(s) removed.")
    else:
        logging.info("Duplicates found:")
        for duplicate_file in duplicate_files:
            logging.info(f"- {duplicate_file}")

if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(description="File Deduplication Script")
    parser.add_argument("--directory", type=str, help="Directory path for deduplication")
    parser.add_argument("--delete", action="store_true", help="Delete duplicate files if set")
    args = parser.parse_args()

    duplicate_files = find_duplicates(args.directory)
    remove_duplicates(duplicate_files, delete=args.delete)
```