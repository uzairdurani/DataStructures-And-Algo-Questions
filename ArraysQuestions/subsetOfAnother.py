def CheckSubset(arr1, arr2, n, m):
    i = 0
    j = 0
    if n < m:
        return 0
    arr1.sort()
    arr2.sort()
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] == arr2[j]:
            j += 1
            i += 1
        elif arr1[i] > arr2[j]:
            return 0
    return True if m == j else False


arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]
n = len(arr1)
m = len(arr2)

print(CheckSubset(arr1, arr2, n, m))
