def Search(arr, x):
    i = 0
    j = len(arr)-1
    while i < len(arr) and j >= 0:
        if arr[i][j] == x:
            return i, j
        if arr[i][j] > x:
            j -= 1
        else:
            i += 1
    return -1


arr = [[1, 2, 3], [5, 6, 7], [7, 8, 9]]
print(Search(arr, 5))
