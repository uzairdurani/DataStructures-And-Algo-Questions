# def editDistance(s1, s2):
#     def newDistance(s1, s2, m, n):
#         if m == 0:
#             return n
#         if n == 0:
#             return m
#         if s1[-1] == s2[-1]:
#             return newDistance(s1, s2, m-1, n-1)
#         return 1+min(newDistance(s1, s2, m, n-1), newDistance(s1, s2, m-1, n), newDistance(s1, s2, m-1, n-1))
#     print(newDistance(s1, s2, len(s1), len(s2)))


def method2(s1, s2):
    def editDistance(s1, s2, m, n):
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                       dp[i-1][j],        # Remove
                                       dp[i-1][j-1])    # Replace
        return dp[-1][-1]
    print(editDistance(s1, s2, len(s1), len(s2)))


s = "sunday"
t = "saturday"
# editDistance(s, t)
method2(s, t)
