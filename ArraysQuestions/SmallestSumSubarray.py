def FindSmallestSubArrays(arr, n, x):
    min_len = len(arr)
    start = 0
    end = 0
    curr_sum = 0
    while end < n:
        while curr_sum <= x and end < n:
            curr_sum += arr[end]
            end += 1
        while curr_sum > x and start < n:
            if end-start < min_len:
                min_len = end-start
            curr_sum -= arr[start]
            start += 1
    return min_len


arr1 = [2, 3, 1, 2, 4, 3]
x = 7
n1 = len(arr1)
res1 = FindSmallestSubArrays(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1)
