

def duplicate(arr, n):
    seen = []
    for i in range(n):
        if arr[i] in seen:
            return arr[i]
        seen.append(arr[i])
    return -1


def store(arr, cur):
    if cur == arr[cur]:
        return cur
    nxt = arr[cur]
    arr[cur] = cur
    return store(arr, nxt)


def printRepeating(arr, size):

    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")


# # arr = [0, 3, 1, 2, 2, 3]
# arr = [1, 1, 3, 4]
# # numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
# arr_size = len(arr)
# for i in range(arr_size):

#     x = arr[i] % arr_size
#     arr[x] = arr[x] + arr_size

# print("The repeating elements are : ")
# for i in range(arr_size):
#     if (arr[i] >= arr_size*2):
#         print(i, " ")

# # n = len(arr)
# # print(duplicate(arr, n))
# # print(store(arr,
# # 0))
# # print(printRepeating(arr, n))


# def printDuplicates(arr, n):

#     fl = 0

#     for i in range(0, n):

#         if (arr[arr[i] % n] >= n):

#             if (arr[arr[i] % n] < 2 * n):
#                 print(arr[i] % n, end=" ")
#                 fl = 1

#         arr[arr[i] % n] += n

    # if (fl == 0):
    #     print("-1")


# Driver Function
arr = [2, 1, 1, 4]
arr_size = len(arr)
printDuplicates(arr, arr_size)
