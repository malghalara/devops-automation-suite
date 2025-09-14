#!/usr/bin/env python3
import os
import shutil

SOURCE_FILE = "sample.txt"
BACKUP_DIR = "backups"

def create_file():
    with open(SOURCE_FILE, "w") as f:
        f.write("This is a sample file created by file_handler.py\n")
    print(f"[INFO] File '{SOURCE_FILE}' created.")

def backup_file():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_path = os.path.join(BACKUP_DIR, SOURCE_FILE)
    shutil.copy(SOURCE_FILE, backup_path)
    print(f"[INFO] File backed up to {backup_path}")

def delete_file():
    if os.path.exists(SOURCE_FILE):
        os.remove(SOURCE_FILE)
        print(f"[INFO] File '{SOURCE_FILE}' deleted.")
    else:
        print(f"[WARNING] File '{SOURCE_FILE}' does not exist.")

if __name__ == "__main__":
    create_file()
    backup_file()
    delete_file()
