def rearrangeArray(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    print(arr)


arr = [-1, 3, 2, 11, -1, 0, -4]

rearrangeArray(arr)
