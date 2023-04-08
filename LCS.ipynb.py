# Dynamic Programming implementation of Longest Common Subsequence problem

def longest_common_subsequence(str1, str2):
    # Find the length of the strings
    len1 = len(str1)
    len2 = len(str2)

    # Declare the array for storing the dp values
    dp_array = [[None] * (len2 + 1) for i in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                dp_array[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp_array[i][j] = dp_array[i-1][j-1] + 1
            else:
                dp_array[i][j] = max(dp_array[i-1][j], dp_array[i][j-1])

    # dp_array[len1][len2] contains the length of LCS of str1[0..len1-1] & str2[0..len2-1]
    return dp_array[len1][len2]

# Driver program to test the above function
str1 = "AGGTAB"
str2 = "GXTXAYB"
print("Length of LCS is ", longest_common_subsequence(str1, str2))