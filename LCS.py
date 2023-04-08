def longest_common_subsequence(x, y):
    # Find the length of the strings
    len1 = len(x)
    len2 = len(y)

    # Declare the array for storing the dp values
    dp_array = [[None] * (len2 + 1) for i in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                dp_array[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp_array[i][j] = dp_array[i-1][j-1] + 1
            else:
                dp_array[i][j] = max(dp_array[i-1][j], dp_array[i][j-1])

    # dp_array[len1][len2] contains the length of LCS of str1[0..len1-1] & str2[0..len2-1]
    return dp_array[len1][len2]