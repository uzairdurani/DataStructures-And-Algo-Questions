def LongestSub(arr, N):
    ans = 1
    count = 0
    arr.sort()
    v = []
    for i in range(N):
        if arr[i] != arr[i-1]:
            v.append(arr[i])

    for i in range(len(v)):
        if i > 0 and v[i] == v[i-1]+1:
            count += 1
        else:
            count = 1

        ans = max(ans, count)

    return ans


arr = [2, 6, 1, 9, 4, 5, 3]
N = len(arr)
print(LongestSub(arr, N))
