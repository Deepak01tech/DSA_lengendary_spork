
def leftMostRepeatingCharacter(s: str) -> int:
    """
    Find the index of the leftmost repeating character in a string.
    If no repeating character exists, return -1.

    :param s: Input string
    :return: Index of the leftmost repeating character or -1 if none exists
    """
    seen = set()
    for i, char in enumerate(s):
        if char in seen:
            return i
        seen.add(char)
    return -1
# Example usage
if __name__ == "__main__":
    test_string = "abca"
    result = leftMostRepeatingCharacter(test_string)
    print(f"The index of the leftmost repeating character in '{test_string}' is: {result}")

    test_string2 = "abcdef"
    result2 = leftMostRepeatingCharacter(test_string2)
    print(f"The index of the leftmost repeating character in '{test_string2}' is: {result2}")