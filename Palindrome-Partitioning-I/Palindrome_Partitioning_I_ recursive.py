def is_palindrome(s, start, end):
    """Check if a substring is a palindrome."""
    while start < end:
        if s[start] != s[end]:
            return False
        start, end = start + 1, end - 1
    return True

def partition(s):
    """Function to partition a string into all possible palindrome partitions."""
    def backtrack(start, path):
        # If we reach the end of the string, add the current partition to the result
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start, len(s)):
            # If the substring s[start:end+1] is a palindrome
            if is_palindrome(s, start, end):
                # Add it to the current path
                path.append(s[start:end+1])
                # Backtrack for the remaining substring
                backtrack(end + 1, path)
                # Backtrack and remove the last palindrome from the current path
                path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    input_string = "abcbdd"
    palindrome_partitions = partition(input_string)
    print(palindrome_partitions)