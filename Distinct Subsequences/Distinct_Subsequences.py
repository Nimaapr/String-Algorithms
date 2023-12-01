def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Edge case: if target string is empty, there is one subsequence in any string
    if n == 0:
        return 1
    
    # Dynamic programming table
    # dp[i][j] will store the number of subsequences in s[:i] which equals t[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # If t is empty, there is one matching subsequence in any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, add the count from previous subsequences
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                # If not matching, carry over the count from previous part of s
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

# Example usage
s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
