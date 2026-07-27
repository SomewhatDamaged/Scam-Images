import os
from create_image_folder import make_folder_from_file
import glob

def main():
    folders = glob.glob(r"../*/")
    print(folders)
    for folder in folders:
        folder: str = folder.replace("\\", "/")
        print(folder)
        if folder.endswith("2025/") or folder.endswith("2026/") or folder.endswith("Image/"):
            path = make_folder_from_file(f"{folder}info.txt")
            if not path:
                continue
            for file in glob.glob(f"{folder}*"):
                file: str = file.replace("\\", "/")
                file = file.rsplit("/", 1)[1]
                print(f"Moving {folder}{file} -> {path}{file}")
                os.rename(f"{folder}{file}", f"{path}{file}")
            os.rmdir(f"{folder}")

if __name__ == "__main__":
    main()