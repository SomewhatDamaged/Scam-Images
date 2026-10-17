import os

from pyrfc3339 import generate
from datetime import datetime, timezone
from random import randint

def make_file(file_path: str) -> bool:
    file_path = str.replace(file_path, ":", "-")
    print(f"making file: {file_path}")
    for _ in range(5):
        try:
            open(file_path, "a").close()
        except OSError:
            continue
        return True
    print("I don't know what to say here. This shouldn't happen. PANIK!")
    return False

def main():
    time: str = generate(datetime.now(tz=timezone.utc))
    file_name: str = f"../strings/{time}-{randint(1000,9999)}.txt"
    make_file(file_name)
    print(f"Made file: {file_name}")

if __name__ == "__main__":
    main()