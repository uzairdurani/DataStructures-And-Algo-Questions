def SwapsRequired(arr, n, k):
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1
    bad = 0
    for i in range(0, count):
        if arr[i] > k:
            bad += 1

    ans = bad
    j = count
    for i in range(n):
        if j == n:
            break
        if arr[i] > k:
            bad = bad - 1
        if arr[j] > k:
            bad = bad+1

        ans = min(ans, bad)
        j += 1

    return ans


arr = [1, 4, 3, 5, 2, 6]
n = len(arr)
k = 4
print(SwapsRequired(arr, n, k))
