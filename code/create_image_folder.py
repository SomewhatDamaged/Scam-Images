import os

from pyrfc3339 import generate
from datetime import datetime, timezone
from random import randint

def make_folder_from_file(file_path) -> str:
    modified_time: float | int = os.path.getmtime(file_path)
    modified_time: datetime = datetime.fromtimestamp(modified_time, timezone.utc)
    modified_time: str = generate(modified_time).replace(":", "-")
    path = f"../images/{modified_time}-{randint(1000,9999)}/"
    if not make_folder(path):
        return ""
    return path

def make_folder(file_path: str) -> bool:
    file_path = str.replace(file_path, ":", "-")
    print(f"making folder: {file_path}")
    for _ in range(5):
        try:
            os.makedirs(file_path)
        except OSError:
            continue
        return True
    print("I don't know what to say here. This shouldn't happen. PANIK!")
    return False

def main():
    time: str = generate(datetime.now(tz=timezone.utc))
    folder_name: str = f"../images/{time}-{randint(1000,9999)}/"
    make_folder(folder_name)
    print(f"Made folder: {folder_name}")

if __name__ == "__main__":
    main()