N = 4


def rotate(arr):
    global N
    for j in range(N):
        for i in range(N - 1, -1, -1):
            print(arr[i][j], end=" ")
        print()


mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
rotate(mat)
