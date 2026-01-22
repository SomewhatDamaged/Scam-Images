# If you need a way to compare two str hashes, this will return an integer of the hamming distance.
# Note: they must be equal length

def hamming_distance(s1: str, s2: str) -> int:
    assert len(s1) == len(s2)
    return bin(int(s1, 16) ^ int(s2, 16)).count("1")
