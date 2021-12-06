def findLongestSubsequence(S):
    n = len(S)
    dp = [[0 for k in range(n+1)] for j in range(n+1)]
    print(dp)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S[j-1] and i != j:

                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp)
    return dp[n][n]


str = "aabb"
print(findLongestSubsequence(str))
