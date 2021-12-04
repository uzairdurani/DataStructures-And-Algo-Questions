def ThreeWays(arr, n, low, high):
    start = 0
    end = n-1
    i = 0
    while i <= end:
        if arr[i] < low:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif arr[i] > high:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1

    return arr


arr = [1, 2, 3, 3, 4, 3]
low, high = 1, 3
n = len(arr)
print(ThreeWays(arr, n, low, high))
