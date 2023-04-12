def longest_common_subsequence(string1, string2, length1, length2):
    if length1 == 0 or length2 == 0:
        return 0
    elif string1[length1-1] == string2[length2-1]:
        return 1 + longest_common_subsequence(string1, string2, length1-1, length2-1)
    else:
        return max(longest_common_subsequence(string1, string2, length1, length2-1),
                   longest_common_subsequence(string1, string2, length1-1, length2))
