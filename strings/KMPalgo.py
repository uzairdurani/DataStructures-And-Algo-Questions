# def longestPrefixSuffix(s):
#     n = len(s)

#     for res in range(n // 2, 0, -1):

#         # Check for shorter lengths
#         # of first half.
#         prefix = s[0: res]
#         suffix = s[n - res: n]

#         if (prefix == suffix):
#             return res

#     # if no prefix and suffix match
#     # occurs
#     return 0


def longestPrefix(s):

    n = len(s)
    lps = [0] * n   # lps[0] is always 0

    l = 0

    i = 1
    while (i < n):
        if (s[i] == s[l]):
            l = l + 1
            lps[i] = l
            i = i + 1

        else:

            if (l != 0):
                l = lps[l-1]

            else:

                lps[i] = 0
                i = i + 1

    res = lps[n-1]

    return res


s = "abab"
print(longestPrefix(s))
