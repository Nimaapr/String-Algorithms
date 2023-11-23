def editDistance(str1, str2):
    m, n = len(str1), len(str2)

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill dp[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, insert all characters of second string
            if i == 0:
                dp[i][j] = j

            # If second string is empty, remove all characters of first string
            elif j == 0:
                dp[i][j] = i

            # If last characters are the same, ignore last character and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character is different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],      # Insert
                                   dp[i - 1][j],      # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    distance = editDistance(str1, str2)
    print(distance)
