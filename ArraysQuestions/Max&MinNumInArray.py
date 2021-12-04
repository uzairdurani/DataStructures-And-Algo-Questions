# def getMaxmini(arr):
#     maxi, mini = 0, 0
#     if arr[0] > arr[1]:
#         maxi = arr[0]
#         mini = arr[1]
#     else:
#         maxi = arr[1]
#         mini = arr[0]

#     for i in range(2, len(arr)):
#         if arr[i] > maxi:
#             maxi = arr[i]
#         elif arr[i] < mini:
#             mini = arr[i]
#     return (maxi, mini)


# def getMaxmini(arr, low, high):
#     maxi, mini = arr[low], arr[low]
#     if low == high:
#         maxi = arr[low]
#         mini = arr[low]

#         return (maxi, mini)
#     elif high == low+1:
#         if arr[low] > arr[high]:
#             maxi = arr[low]
#             mini = arr[high]
#         else:
#             maxi = arr[high]
#             mini = arr[low]

#         return (maxi, mini)
#     else:
#         mid = int((low + high) / 2)
#         arr1_max, arr1_min = getMaxmini(arr, low, mid)
#         arr2_max, arr2_mini = getMaxmini(arr, mid+1, high)

#     return (max(arr1_max, arr2_max), min(arr1_min, arr2_mini))


def getMaxmin(arr):

    n = len(arr)

    if n % 2 == 0:
        maxi = max(arr[0], arr[1])
        mini = min(arr[0], arr[1])
        i = 2
    else:
        maxi = mini = arr[0]
        i = 1

    while i < n-1:
        if arr[i] < arr[i+1]:
            maxi = max(maxi, arr[i+1])
            mini = min(mini, arr[i])
        else:
            maxi = max(maxi, arr[i])
            mini = min(mini, arr[i+1])

        i += 2
    return maxi, mini


arr = [1, 2, 3, 4, 4, 5]
print(getMaxmin(arr))
