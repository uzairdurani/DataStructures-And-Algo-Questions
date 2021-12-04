def method1(arr):
    if len(arr) % 2 == 0:
        mid = len(arr)//2
        mid_value = arr[mid]
        mide_minus_1 = arr[mid]
        ans = (mid_value+mide_minus_1)/2
        return ans

    else:
        mid = len(arr)//2
        ans = arr[mid]
        return ans


def method2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    if n > m:
        method2(arr2, arr1)

    start = 0
    end = n
    realmidinmergedarray = (n+m+1)//2
    while start <= end:
        mid = (start+end)//2
        leftASize = mid
        leftBSize = realmidinmergedarray - mid
        leftA = arr1[leftASize-1] if (leftASize > 0) else float('-inf')
        leftB = arr2[leftASize - 1] if (leftBSize > 0) else float('-inf')

        rightA = arr1[leftASize] if (leftASize < n) else float('inf')
        rightB = arr1[leftASize] if (leftBSize < m) else float('inf')

        if leftA <= rightB and leftB <= rightA:
            if ((m + n) % 2 == 0):
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            return max(leftA, leftB)
        elif (leftA > rightB):
            end = mid - 1
        else:
            start = mid + 1


if __name__ == "__main__":

    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]

    # Concatenating the two arrays
    arr3 = arr1 + arr2

    # Sorting the resultant array
    arr3.sort()

    print("Median = ", method2(arr1, arr2))
