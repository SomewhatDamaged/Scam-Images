import glob

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
    list_ = glob.glob(r"./scam_images/*/*")
    for target in list_:
        if hash := get_phash(target):
            hashes.append(hash)
    hash_string = '","'.join(hashes)
    print(f'["{hash_string}"]')


if __name__ == "__main__":
    main()
