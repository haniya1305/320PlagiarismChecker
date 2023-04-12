def longest_common_subsequence(seq1, seq2, len1, len2):
    # Declaring the array for storing the dp values
    lcs_array = [[None]*(len2+1) for i in range(len1+1)]

    # Following steps build lcs_array[len1+1][len2+1] in bottom up fashion
    # Note: lcs_array[i][j] contains length of LCS of seq1[0..i-1] and seq2[0..j-1]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                lcs_array[i][j] = 0
            elif seq1[i-1] == seq2[j-1]:
                lcs_array[i][j] = lcs_array[i-1][j-1] + 1
            else:
                lcs_array[i][j] = max(lcs_array[i-1][j], lcs_array[i][j-1])

    # lcs_array[len1][len2] contains the length of LCS of seq1[0..len1-1] and seq2[0..len2-1]
    return lcs_array[len1][len2]
#%%
