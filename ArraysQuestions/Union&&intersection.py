def union(arr1, arr2):
    i = j = 0
    n = len(arr1)
    m = len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=' ')
            i += 1
        elif arr1[j] > arr2[i]:
            print(arr2[j], end=' ')
            j += 1
        else:
            print(arr1[i], end=' ')
            i += 1
            j += 1

    while i < n:
        print(arr1[i], end=' ')
        i += 1
    while j < m:
        print(arr2[j], end=' ')
        j += 1

    print()


def UnionOfArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    newtable = [0] * (max(max(arr1), max(arr2))+1)
    print(arr1[0], end=' ')
    newtable[arr1[0]] += 1
    for i in range(1, len(arr1)):
        if arr1[i] != arr1[i - 1]:
            print(arr1[i], end=" ")
            newtable[arr1[i]] += 1

    for j in range(0, len(arr2)):
        # By checking whether it's already
        # present in newtable or not
        if newtable[arr2[j]] == 0:

            print(arr2[j], end=" ")
            newtable[arr2[j]] += 1


def intersectionOfArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr1[i])
            i += 1
            j += 1


arr1 = [0, 1, 3, 5, 7, 2]
arr2 = [3, 5, 0, 8]
# UnionOfArrays(arr1, arr2)
intersectionOfArrays(arr1, arr2)
