def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    if n == 0:
        return 1
    
    dp_previous = [1] + [0] * n
    dp_current = [1] + [0] * n

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp_current[j] = dp_previous[j - 1] + dp_previous[j]
            else:
                dp_current[j] = dp_previous[j]

        dp_previous, dp_current = dp_current, [1] + [0] * n

    return dp_previous[n]


# Example usage
s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
