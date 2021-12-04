

def countInversions(arr):
    inv_count = 0
    if len(arr) > 1:
        mid = (len(arr))//2
        l = arr[:mid]
        r = arr[mid:]
        inv_count += countInversions(l)
        inv_count += countInversions(r)
        i, j, k = 0, 0, 0
        temp_arr = [0]*len(arr)
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                temp_arr[k] = l[i]
                i += 1

            else:
                temp_arr[k] = r[j]
                inv_count += len(temp_arr)
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            k += 1
            i += 1

        while j < len(r):
            arr[k] = r[j]
            k += 1
            j += 1
        for i in range(len(temp_arr)):
            arr[i] = temp_arr[i]
    return inv_count


arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462,
       492, 496, 443, 328, 437, 392,
       105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370,
       413, 168, 300, 36, 395, 204, 312, 323]
n = len(arr)
result = countInversions(arr)
print("Number of inversions are", result)


print(n)
