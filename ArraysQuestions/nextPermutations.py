def nextPermutation(arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        arr.sort()
        return arr
    k = i-1
    j = len(arr)-1
    while j > k and arr[k] >= arr[j]:
        j -= 1
    arr[j], arr[k] = arr[k], arr[j]
    l = k+1
    r = len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


arr = [1, 3, 2]

print(nextPermutation(arr))
