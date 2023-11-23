def editDistance(str1, str2):
    m, n = len(str1), len(str2)

    # Create two arrays for storing the current and previous rows
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Initialize the previous row
    for j in range(n + 1):
        prev[j] = j

    for i in range(1, m + 1):
        # Current row first element equals the row number
        curr[0] = i

        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(curr[j - 1],      # Insert
                                  prev[j],          # Remove
                                  prev[j - 1])      # Replace

        # Swap the current and previous row for the next iteration.
        # After this swap, prev holds the most recent results (which was curr),
        # and curr becomes a recycled array for the next iteration's calculations.
        prev, curr = curr, prev

    # The result is in the last element of the previous row
    return prev[n]



if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    distance = editDistance(str1, str2)
    print(distance)