def find_first_non_repeating(string):
    """
    Find the first non-repeating character in a string.
    :param string: a string of characters.
    :return: the first character that does not repeat itself in the string.
    """
    # Creating a dictionary to store character frequency
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Find the first non-repeating character
    for char in string:
        if char_frequency[char] == 1:
            return char

    return None  # Return None if all characters are repeating


if __name__ == "__main__":
    test_string = input("Enter a string: ")
    result = find_first_non_repeating(test_string)
    if result:
        print(f"The first non-repeating character is: {result}")
    else:
        print("All characters are repeating.")
