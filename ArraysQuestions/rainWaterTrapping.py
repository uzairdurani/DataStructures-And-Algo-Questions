def M1RainCount(arr, n):
    res = 0
    for i in range(1, n):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        res = res + (min(left, right) - arr[i])
    print(res)


def M2RainCount(arr, n):
    water = 0
    left = [0]*n
    right = [0]*n
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(arr[i], left[i-1])
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    for j in range(n):
        water += min(left[j], right[j])-arr[j]
    print(water)


arr = [0, 1, 0, 2, 1, 0,
       1, 3, 2, 1, 2, 1]
n = len(arr)
# M1RainCount(arr, n)
M2RainCount(arr, n)
