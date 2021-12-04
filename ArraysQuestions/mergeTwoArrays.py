from math import inf


def merge(arr1, arr2, m, n):
    for i in range(n-1, -1, -1):
        last = arr1[m-1]  # last index
        j = m-2  # second last
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j+1] = arr1[j]
            j -= 1

        if j != m-2 or last > arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last


def merge(arr1, arr2, n, m):
    i = n-1
    j = 0
    while(i >= 0 and j < m):
        if(arr1[i] > arr2[j]):
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp
        i = i-1
        j = j+1
    arr1.sort()
    arr2.sort()


ar1 = [1, 2, 3, 0, 0, 0]
ar2 = [2, 5, 6]
n = len(ar1)-1
m = len(ar2)-1

merge(ar1, ar2, n, m)
print(ar1, ar2)
