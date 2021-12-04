def ReArrange(arr, n):
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])

    i, j, k = 0, 0, 0
    while i < len(neg) and j < len(pos):
        arr[k] = pos[j]
        j += 1
        k += 1
        arr[k] = neg[i]
        i += 1
        k += 1

    while j < len(pos):
        arr[k] = pos[j]
        j += 1  
        k += 1
    while i < len(neg):
        arr[k] = neg[i]
        i += 1
        k += 1

    return arr


# def reArrange(arr):
#     i = -1
#     for j in range(len(arr)):
#         if arr[j] < 0:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     pos, neg = i+1, 0
#     while (pos < len(arr) and neg < pos and arr[neg] < 0):
#         arr[neg], arr[pos] = arr[pos], arr[neg]
#         pos += 1
#         neg += 2
# def Arrange(arr):
#     arr.sort()
#     i, j = 1, 1
#     while j < len(arr):
#         if arr[j] > 0:
#             break
#         j += 1
#     while arr[i] < 0 and j < len(arr):
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 2
#         j += 1
#     return arr
# =
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
ReArrange(arr, len(arr))
print(arr)
