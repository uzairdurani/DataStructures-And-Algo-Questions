import sys


def findMaxPair(arr, N):
    max_value = -sys.maxsize-1
    max_arr = [[0 for x in range(N)] for y in range(N)]
    max_arr[N-1][N-1] = arr[N-1][N-1]

    maxv = arr[N-1][N-1]
    # preprocess last row
    for j in range(N-2, -1, -1):
        if arr[N-1][j] > maxv:
            maxv = arr[N-1][j]
        max_arr[N-1][j] = maxv

    # proprocess last columns
    maxv = arr[N - 1][N - 1]  # Initialize max
    for i in range(N - 2, -1, -1):

        if (arr[i][N - 1] > maxv):
            maxv = arr[i][N - 1]
        max_arr[i][N - 1] = maxv

    # preprocess rest of the matrix
    # from bottom

    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            # Update max_value
            # Update max_value
            if (max_arr[i + 1][j + 1] -
                    arr[i][j] > max_value):
                max_value = (max_arr[i + 1][j + 1] -
                             arr[i][j])
              # set maxArr (i, j)
            max_arr[i][j] = max(arr[i][j],
                                max(max_arr[i][j + 1],
                                    max_arr[i + 1][j]))
    return max_value


mat = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]
print(*mat)
print(findMaxPair(mat, len(mat)))
