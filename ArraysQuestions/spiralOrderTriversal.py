def spiralOrderPrint(arr, row_end, col_end):
    n = len(arr)
    row_st = 0
    col_st = 0

    while row_st < row_end and col_st < col_end:
        # row start
        for i in range(col_st, col_end):
            print(arr[row_st][i], end=' ')
        row_st += 1


# colend
        for last in range(row_st, row_end):
            print(arr[last][col_end-1], end=' ')
        col_end -= 1

# rowend

        if row_st < row_end:

            for i in range(col_end-1, col_st-1, -1):
                print(arr[row_end-1][i], end=' ')

            row_end -= 1

        if col_st < col_end:
            for i in range(row_end-1, row_st-1, -1):
                print(arr[i][col_st], end=' ')

            col_st += 1

    return 0


arr = [[1, 2, 3, 4, 5, 6],
       [7, 8, 9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18]]
row_end = len(arr)
col_end = len(arr[0])
spiralOrderPrint(arr, row_end, col_end)
