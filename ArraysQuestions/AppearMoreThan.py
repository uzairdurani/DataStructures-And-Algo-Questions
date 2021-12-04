def MoreThanN(arr, N, k):
    x = N//k
    freq = {}
    for i in range(N):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    for i in freq:
        if freq[i] > x:
            print(i)


arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
n = len(arr)
k = 4
MoreThanN(arr, n, k)
