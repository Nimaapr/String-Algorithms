def partition(s):
    n = len(s)

    # dp[i][j] will be True if the string from index i to j is a palindrome.
    dp = [[False] * n for _ in range(n)]

    # Pre-compute the palindrome table.
    for end in range(n):
        for start in range(end + 1):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True

    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return

        for end in range(start, n):
            if dp[start][end]:
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    input_string = "abcbdd"
    palindrome_partitions = partition(input_string)
    print(palindrome_partitions)