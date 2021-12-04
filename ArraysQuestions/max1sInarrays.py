def MaxOnes(arr):
    maxCount = 0
    maxindex = -1
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1

        if count > maxCount:
            maxCount = count
            maxindex = i
    print(maxCount, maxindex)


def method2(arr, n, m):
    max_index = -1
    max_count = 0
    curr_col = m-1
    for i in range(n):
        while curr_col >= 0 and arr[i][curr_col] == 1:
            curr_col = curr_col - 1
            max_index = i

    return -1 if max_index == -1 else max_index


mat = [[1, 1, 1, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

MaxOnes(mat)
print(method2(mat, len(mat), len(mat[0])))
