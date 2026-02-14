import glob
import json

import imagehash
from PIL import Image

# Generates a list of hashes based on a folder "scam_images" with a list of folders containing images within it.


def get_phash(filename: str) -> str:
    output = ""
    try:
        img = Image.open(filename)
        output = str(imagehash.phash(img, hash_size=16))
    finally:
        return output


def main() -> None:
    hashes = []
    list_ = glob.glob(r"./*/*")
    print(list_)
    for target in list_:  # Build list
        if hash := get_phash(target):
            hashes.append(hash)
    hashes = list(set(hashes))  # Remove dupes
    hash_string = '","'.join(hashes)
    print(f'["{hash_string}"]')
    with open("hashes.json", "w") as hash_file:
        json.dump(hashes, hash_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
