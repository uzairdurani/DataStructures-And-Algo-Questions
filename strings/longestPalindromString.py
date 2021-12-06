def longestPalSubstr(S):
    res = ""
    resLen = 0

    for i in range(len(S)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if(r-l+1) > resLen:
                res = S[l:r+1]
                resLen = r-l+1
            print(resLen, res)
            l -= 1
            r += 1
        # even length
        l, r = i, i+1
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if(r-l+1) > resLen:
                res = S[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1
    return res


print(longestPalSubstr('geeks'))
