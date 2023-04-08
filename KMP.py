def KMP(p, t):
    M = len(p)  # length of pattern is M
    N = len(t)  # length of text is N
    # initialization
    pi = [0] * M
    j = 0
    # calculate pi table for the pattern
    PiTable(p, M, pi)
    i = 0  # index for text to iterate over
    while (N - i) >= (M - j):
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == M:
            print("Pattern matched at index " + str(i - j))
            j = pi[j - 1]
        # mismatch after j matches
        elif i < N and p[j] != t[i]:
            # Do not match pi[0..pi[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1

def PiTable(pat, M, pi):
    sub = 0  # length of the previous longest prefix suffix
    pi[0] = 0  # lps[0] is always 0
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[sub]:
            sub += 1
            pi[i] = sub
            i += 1
        else:
            if sub != 0:
                sub = pi[sub - 1]
                # Also, note that we do not increment i here
            else:
                pi[i] = 0
                i += 1