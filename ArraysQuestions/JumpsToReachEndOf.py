# from math import inf


# def minJumps(arr, n):
#     # code here
#     jumps = [0 for i in range(n)]
#     if n <= 1:
#         return 0
#     elif arr[0] == 0:
#         return -1
#     else:
#         jumps[0] = 0
#         for i in range(1, n):
#             jumps[i] = inf
#             for j in range(i):
#                 if i <= j+arr[j] and jumps[j] != inf:
#                     jumps[i] = min(jumps[i], jumps[j]+1)
#                     # break
#         if jumps[n-1] == inf:
#             jumps[n-1] = -1
#         return jumps[n-1]


def minJumps(arr, n):
    mx = arr[0]
    step = arr[0]
    jumps = 1
    if n == 1:
        return 0
    elif arr[0] == 0:
        return -1
    else:
        for i in range(1, n-1):
            mx = max(mx, i+arr[i])
            step -= 1
            if step == 0:
                if i >= mx:
                    return -1
                step = mx - i
                jumps += 1
        return jumps


# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
arr = [2, 1, 0, 3]
arr = [2, 1, 1, 3]
n = len(arr)
print(minJumps(arr, n))
