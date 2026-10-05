import os

from build_list import get_filenames, get_phash_and_dimensions
from build_list import main as process_hashes

def main() -> None:
    hashes = []
    i = 0
    files = get_filenames()
    for target in files:
        result = get_phash_and_dimensions(target)
        if not result:
            continue
        remove = True
        multi = False
        if len(result) > 1:
            for phash, _ in result:
                if phash not in hashes:
                    remove = False
                hashes.append(phash)
            multi = True
        else:
            if result[0][0] not in hashes:
                remove = False
            hashes.append(result[0][0])
        if remove:
            i += 1
            print("Removing", target, " Multi: ", multi)
            os.remove(target)
    print("Removed", i, " of ", len(files), "\nKept: ", len(files)-i)
    proceed = input("Would you like to upload? (y/n): ")
    if proceed == "y":
        process_hashes(True)




if __name__ == "__main__":
    main()