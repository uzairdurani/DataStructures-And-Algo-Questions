def median(arr1, arr2, n):
    i, j = 0, 0
    m1, m2 = -1, -1
    count = 0
    while count < n+1:
        count += 1
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break

        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1

        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m1+m2)/2


def getMedian(ar1, ar2, n):
    i, j = n - 1, 0

    # while loop to swap all smaller numbers to arr1
    while(ar1[i] > ar2[j] and i > -1 and j < n):
        ar1[i], ar2[j] = ar2[j], ar1[i]
        i -= 1
        j += 1

    ar1.sort()
    ar2.sort()

    return (ar1[-1] + ar2[0]) >> 1


ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ", median(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")
print(getMedian(ar1, ar2, n1))
