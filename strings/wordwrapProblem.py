import sys


def SolveWordWrap(arr, n, k):
    dp = [0] * n

    ans = [0] * n

    dp[n - 1] = 0
    ans[n - 1] = n - 1

    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = sys.maxsize

        for j in range(i, n):

            currlen += (arr[j] + 1)

            if (currlen > k):
                break

            if (j == n - 1):
                cost = 0
            else:
                cost = ((k - currlen) *
                        (k - currlen) + dp[j + 1])
                print(cost, currlen)

            if (cost < dp[i]):
                dp[i] = cost
                ans[i] = j
    print(dp, ans)

    # i = 0
    # while (i < n):
    #     print(i + 1, ans[i] + 1, end=" ")
    #     i = ans[i] + 1
    print(dp[0])


arr = [3, 2, 2]
n = len(arr)

SolveWordWrap(arr, n, 4)
