def nextPermutation(n, arr):
    # code here
    k = n-2
    while k >= 0:
        if arr[k] < arr[k+1]:
            break
        k -= 1
    if k < 0:
        arr = arr[::-1]
    else:
        for l in range(n-1, k, -1):
            if arr[l] > arr[k]:
                break
        arr[l], arr[k] = arr[k], arr[l]
        arr[k+1:] = reversed(arr[k+1:])
    return arr


x = ['1', '2', '3', '4']
print(nextPermutation(len(x), x))
