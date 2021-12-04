

from sys import maxsize


def LargestSubarray(arr):
    maxSoFor = -9999999999999
    maxEnd = 0

    for i in range(len(arr)):
        maxEnd = maxEnd+arr[i]
        if maxSoFor < maxEnd:
            maxSoFor = maxEnd
        if maxEnd < 0:
            maxEnd = 0

    return maxSoFor


def negativeElements(arr):
    maxi = arr[0]
    maxend = arr[0]
    for i in range(len(arr)):
        maxend = max(maxend, maxend+arr[i])
        maxi = max(maxend, maxi)
    return maxi


# arr = [-1, -2, -3, -4]
# arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(LargestSubarray(arr))
# print(negativeElements(arr))
