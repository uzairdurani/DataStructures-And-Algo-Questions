def duplicateArray(arr):
    mp = {}
    for i in range(len(arr[0])):
        mp[arr[0][i]] = 1

    for i in range(1, len(arr)):
        for j in range(len(arr[i])):

            # If element is present in the
            # map and is not duplicated in
            # current row.
            if (mat[i][j] in mp.keys() and
                    mp[mat[i][j]] == i):

                # we increment count of the
                # element in map by 1
                mp[mat[i][j]] = i + 1

                # If this is last row
                if i == len(arr) - 1:
                    print(mat[i][j], end=" ")


mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

duplicateArray(mat)
